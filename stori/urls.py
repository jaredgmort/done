from django.urls import path
from . import views


app_name = 'stori'

urlpatterns = [
	path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('congrats', views.congrats, name='congrats'),
    path('save', views.save, name='save'),
    path('account', views.account, name='account'),
    path('login', views.login, name='login'),
]
