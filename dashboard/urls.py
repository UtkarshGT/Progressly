from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.explore, name='explore'),
    path('<int:roadmap_id>/', views.roadmap_detail, name='roadmap'),
]