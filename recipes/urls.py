from django.urls import path
from . import views


app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),
    # the <int:id> will receive a value according to the parameter of the recipe function in views.py
    path('recipes/<int:id>/', views.recipe, name="recipe"),
]
