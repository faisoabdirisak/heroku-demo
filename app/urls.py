from django.urls import path;
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('math/', views.math, name='math'),
    path('read/', views.read, name='read'),
    path('color/', views.color, name='color'),
    path('environment/', views.environment, name='environment'),
    path('computer/', views.comp, name='comp'),
    path('religion/', views.religion, name='religion'),
   
    # path('submit_review/', views.submit_review, name='submit_review'),
    
    
]