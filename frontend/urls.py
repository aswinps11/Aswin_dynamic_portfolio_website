from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio/<int:pk>/', views.portfolio_details, name='portfolio_details'),
    path('service/<int:pk>/', views.service_details, name='service_details'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
    path('starter/', views.starter_page, name='starter_page'),
]