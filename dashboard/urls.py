from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.explore, name='explore'),
    path('<int:pk>/', views.roadmap_detail, name='roadmap'),
    path('create-roadmap/', views.roadmap_form, name='roadmap-create'),
    path('update/<int:pk>/', views.roadmap_update, name='roadmap-edit'),
    path('delete/<int:pk>/', views.roadmap_delete, name='roadmap-delete'),

    path('create-entity/', views.entity_form, name='entity-create'),
    path('update-entity/<int:pk>/', views.entity_update, name='entity-edit'),
    path('delete-entity/<int:pk>/', views.entity_delete, name='entity-delete'),
]