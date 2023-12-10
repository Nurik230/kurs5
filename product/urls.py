from django.urls import path
from .views import ProductListAPIView, ProductDetailAPIView, ReviewListAPIView, ReviewDetailAPIView, \
    CategoryListAPIView, CategoryDetailAPIView, ProductReviewAPIView

# from product.views import reviews_list_api_view, category_list_api_view, product_detail_api_view, \
#     category_detail_api_view, reviews_detail_api_view, product_reviews_list_api_view

# urlpatterns = [
#     path('product/', product_list_api_view),
#     path('category/', category_list_api_view),
#     path('reviews/', reviews_list_api_view),
#     path('product/<int:id>/', product_detail_api_view),
#     path('category/<int:id>/', category_detail_api_view),
#     path('reviews/<int:id>/', reviews_detail_api_view),
#     path('product/reviews/', product_reviews_list_api_view)
# ]

urlpatterns = [
    path('product/', ProductListAPIView.as_view()),
    path('category/', CategoryListAPIView.as_view()),
    path('reviews/', ReviewListAPIView.as_view()),
    path('product/<int:pk>/', ProductDetailAPIView.as_view()),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view()),
    path('reviews/<int:pk>/', ReviewDetailAPIView.as_view()),
    path('product/reviews/',  ProductReviewAPIView.as_view())
]
