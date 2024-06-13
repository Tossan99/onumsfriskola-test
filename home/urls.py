from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_home, name='home'),
    path('dokument', views.view_documents, name='documents'),
]