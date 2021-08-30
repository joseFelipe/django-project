from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='cliente'),
    path('detalhe/<int:pk>/', views.detail, name="detalhe"),
    path('edit/<int:pk>/', views.edit, name="edit"),
    path('update/<int:pk>/', views.update, name="update"),
    path('delete/<int:pk>/', views.delete, name="delete"),
    path('form/', views.form, name='form'),
    path('create/', views.create, name='create'),
]
