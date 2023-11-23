from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Product, Review, Category
from product.serializers import ProductSerializers, ReviewSerializers, CategorySerializers, ProductReviewSerializer


@api_view(['GET'])
def product_list_api_view(request):
    if request.method == 'GET':
        product = Product.objects.all()
        serializers = ProductSerializers(product, many=True)
        return Response(serializers.data, status.HTTP_200_OK)


@api_view(['GET'])
def product_detail_api_view(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)
        serializers = ProductSerializers(product)
        return Response(serializers.data, status.HTTP_200_OK)


@api_view(['GET'])
def reviews_list_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializers = ReviewSerializers(reviews, many=True)
        return Response(serializers.data, status.HTTP_200_OK)


@api_view(['GET'])
def reviews_detail_api_view(request, id):
    if request.method == 'GET':
        reviews = Review.objects.get(id=id)
        serializers = ReviewSerializers(reviews)
        return Response(serializers.data, status.HTTP_200_OK)


@api_view(['GET'])
def category_list_api_view(request):
    if request.method == 'GET':
        category = Category.objects.all()
        serializers = CategorySerializers(category, many=True)
        return Response(serializers.data, status.HTTP_200_OK)


@api_view(['GET'])
def category_detail_api_view(request, id):
    if request.method == 'GET':
        category = Category.objects.get(id=id)
        serializers = CategorySerializers(category)
        return Response(serializers.data, status.HTTP_200_OK)

@api_view(['GET'])
def product_reviews_list_api_view(request):
    if request.method == 'GET':
        product = Product.objects.all()
        serializers = ProductReviewSerializer(product, many=True)
        return Response(serializers.data, status.HTTP_200_OK)