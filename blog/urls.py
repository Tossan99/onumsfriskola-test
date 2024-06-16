from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_all_school_classes, name='school_classes'),
    path('<slug:slug>/', views.view_school_class, name='school_class'),
]