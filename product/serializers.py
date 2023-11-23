from rest_framework import serializers

from product.models import Category, Product, Review


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category

        fields = ('id', 'name')

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'description', 'price', 'category')

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review

        fields = ('id', 'text', 'product')





