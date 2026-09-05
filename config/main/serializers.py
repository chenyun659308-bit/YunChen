from rest_framework import serializers
from .models import Contract, Product

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ['name', 'phone', 'email', 'title', 'content']


class ProductSerializer(serializers.ModelSerializer):
    specs = serializers.SerializerMethodField()
    specs_en = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id', 'category', 'name', 'name_en',
            'desc', 'desc_en', 'specs', 'specs_en',
            'image_url', 'sort_order', 'active'
        ]

    def get_specs(self, obj):
        return obj.specs_list

    def get_specs_en(self, obj):
        return obj.specs_en_list

    def get_image_url(self, obj):
        return obj.image_url
