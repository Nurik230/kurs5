from django.urls import path
from . import views

urlpatterns = [
    path('users/register/', views.register_api_view),
    path('users/login/', views.login_api_view),
    path('users/confirm/', views.confirm_user_api_view)
]