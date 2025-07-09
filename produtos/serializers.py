from rest_framework import serializers
from .models import Product, Category, Store, Price


class ProductSerializer(serializers.ModelSerializer):

    category = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "category",
            "user",
            "created_at",
        ]

    def get_category(self, obj):
        return obj.category.name if obj.category else None


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = "__all__"


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = "__all__"
