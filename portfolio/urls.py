from django.urls import path
from .import views

urlpatterns = [
    path('', views.HomePage, name='HomePage'),
    path('home/', views.HomePage, name='HomePage'),
    path('about/', views.AboutPage, name='AboutPage'),

]