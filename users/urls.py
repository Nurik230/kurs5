from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('users/register/', views.register_api_view),
#     path('users/login/', views.login_api_view),
#     path('users/confirm/', views.confirm_user_api_view)
# ]

from .views import RegisterAPIView, LoginAPIView, ConfirmAPIView
urlpatterns = [
    path('users/register/', RegisterAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view()),
    path('users/confirm/', ConfirmAPIView.as_view()),
]