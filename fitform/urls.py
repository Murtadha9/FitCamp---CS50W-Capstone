from django.urls import path
from . import views

urlpatterns=[
    path("", views.indexform, name="indexform"),
    path("homeform", views.homeform, name="homeform"),
    path("loginform", views.loginform, name="loginform"),
    path("logoutform", views.logoutform, name="logoutform"),
    path("registerform", views.registerform, name="registerform"),

    path("body", views.body, name="body"),



    path('category/<int:category_id>/', views.category_exercises, name='category_exercises'),

    path('search/', views.search, name='search'),

    path('fitness/', views.fitness, name='fitness'),
    path('search_fitness/', views.search_fitness, name='search_fitness'),
    path('fitness/<int:fitness_id>/', views.fitness_details, name='fitness_details'),
    path('help', views.help, name='help'),
    path('recived', views.recived, name='recived'),




]
