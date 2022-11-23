from django.urls import path
from . import views


app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),
    # the <int:id> will receive a value according to the parameter of the recipe function in views.py
    path('recipes/search/', views.search, name="search"),
    path('recipes/<int:id>/', views.recipe, name="recipe"),
    path('recipes/category/<int:category_id>/', views.category, name="category"),
]
