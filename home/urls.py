from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_home, name='home'),
    path('dokument/', views.view_documents, name='documents'),
    path('skolan/', views.view_about, name='about'),
    path('personal/', views.view_staff, name='staff'),
]