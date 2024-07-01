from django.urls import path
from . import views


app_name = 'oaauth'

urlpatterns = [
    path('login', views.LoginView.as_view(), name='login'),
    path('resetpwd', views.ResetPassword.as_view(), name='resetpwd')
]