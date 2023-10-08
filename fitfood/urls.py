from django.urls import path 
from . import views

urlpatterns = [
    path("", views.indexfood, name="indexfood"),
    path("homefood", views.homefood, name="homefood"),
    path("loginfood", views.loginfood, name="loginfood"),
    path("logoutfood", views.logoutfood, name="logoutfood"),
    path("registerfood", views.registerfood, name="registerfood"),


    ########################

    path('category/<int:id>/', views.category, name='category'),
    path('vegan/', views.vegan, name='vegan'),
    path('vegetarian/', views.vegetarian, name='vegetarian'),
    path('sweet/', views.sweet, name='sweet'),
    path('high-protein/', views.high_protein, name='high_protein'),
    path('seafood/', views.seafood, name='seafood'),
    path('salad/', views.salad, name='salad'),
    path('low-carbs/', views.low_carbs, name='low_carbs'),
    path('pasta/', views.pasta, name='pasta'),

    
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('recommended/', views.recommended, name='recommended'),

    

]


