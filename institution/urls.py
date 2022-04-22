from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.index, name='institution'),
    path('<int:pk>/', views.roadmap_detail, name='inst_detail'),
    path('<int:pk>/followers/', views.followers, name='followers'),
    path('request/', views.form_institute, name='inst_form'),
    path('follow/', views.follow_roadmap, name='follow'),
    path('unfollow/<int:pk>/', views.unfollow_roadmap, name='unfollow'),
]