from django.urls import path
from . import views

urlpatterns = [ 
    path ('members/', views.members, name = 'members'),
    path ('members/details/<int:id>/', views.details, name = 'details'),
    path ('', views.main, name = 'main'),
    path ('test/', views.test, name = 'test'),
    path ('template/', views.template, name = 'testing'),
]