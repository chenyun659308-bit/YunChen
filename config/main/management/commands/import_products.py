import json
import subprocess
from pathlib import Path

from django.conf import settings
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from main.models import Product


class Command(BaseCommand):
    help = 'Import existing frontend products.js data into the Product model'

    def handle(self, *args, **options):
        js_path = Path(settings.BASE_DIR).parent / 'frontend' / 'src' / 'data' / 'products.js'
        if not js_path.exists():
            self.stderr.write(f'products.js not found: {js_path}')
            return

        node_code = (
            "import { products, products_en } from '"
            + js_path.resolve().as_uri()
            + "'; console.log(JSON.stringify({ products, products_en }));"
        )
        result = subprocess.run(
            ['node', '--input-type=module', '-e', node_code],
            capture_output=True,
        )
        if result.returncode != 0:
            self.stderr.write(result.stderr.decode('utf-8', errors='replace'))
            return

        data = json.loads(result.stdout.decode('utf-8'))
        front_public = js_path.parent.parent.parent / 'public'
        media_root = Path(settings.MEDIA_ROOT)
        created_count = 0
        updated_count = 0

        for item in data['products']:
            product_id = int(item['id'])
            en = data.get('products_en', {}).get(str(product_id), {}) or {}
            defaults = {
                'name': item.get('name', ''),
                'name_en': en.get('name_en', ''),
                'category': item.get('category', ''),
                'desc': item.get('desc', ''),
                'desc_en': en.get('desc_en', ''),
                'specs': '\n'.join(item.get('specs') or []),
                'specs_en': '\n'.join(en.get('specs_en') or []),
                'legacy_image': item.get('image', ''),
                'sort_order': product_id,
                'active': True,
            }
            product, created = Product.objects.update_or_create(
                id=product_id,
                defaults=defaults,
            )
            created_count += created
            updated_count += not created

            if not product.image:
                legacy = (item.get('image') or '').lstrip('/')
                source = front_public / legacy
                if source.exists():
                    with source.open('rb') as image_file:
                        product.image.save(legacy, ContentFile(image_file.read()), save=True)
                    self.stdout.write(f'Copied image: {legacy}')

        self.stdout.write(
            self.style.SUCCESS(f'Import done: {created_count} created, {updated_count} updated')
        )
