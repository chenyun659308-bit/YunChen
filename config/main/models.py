from django.db import models

class Contract(models.Model):
    name = models.CharField('姓名', max_length=50)
    phone = models.CharField('手机号', max_length=20)
    email = models.EmailField('邮箱', max_length=100, blank=True, null=True)
    title = models.CharField('主题', max_length=200)
    content = models.TextField('留言内容')
    created_at = models.DateTimeField('提交时间', auto_now_add=True)

    class Meta:
        db_table = 'contract'
        verbose_name = '留言表单'
        verbose_name_plural = '留言管理'

    def __str__(self):
        return f'{self.name} - {self.title}'


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('冷暖净风器', '冷暖净风器'),
        ('电风扇', '电风扇'),
        ('暖风机', '暖风机'),
        ('小太阳', '小太阳'),
    ]

    name = models.CharField('产品名称', max_length=100)
    name_en = models.CharField('英文名称', max_length=100, blank=True)
    category = models.CharField('产品类型', max_length=50, choices=CATEGORY_CHOICES, default='电风扇')
    desc = models.TextField('产品描述', blank=True)
    desc_en = models.TextField('英文描述', blank=True)
    specs = models.TextField('中文规格（每行一条）', blank=True)
    specs_en = models.TextField('英文规格（每行一条）', blank=True)
    image = models.FileField('产品图片', upload_to='products/', blank=True)
    legacy_image = models.CharField('图片路径', max_length=300, blank=True,
                                    help_text='当未上传新图片时使用，例如 /products/LN01.jpg')
    sort_order = models.IntegerField('排序', default=0)
    active = models.BooleanField('上架', default=True)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table = 'product'
        ordering = ['sort_order', 'id']
        verbose_name = '产品'
        verbose_name_plural = '产品管理'

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return self.legacy_image

    @property
    def specs_list(self):
        return [line.strip() for line in (self.specs or '').splitlines() if line.strip()]

    @property
    def specs_en_list(self):
        return [line.strip() for line in (self.specs_en or '').splitlines() if line.strip()]
