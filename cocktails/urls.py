"""cocktails URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path
from django.views.i18n import JavaScriptCatalog

from app.views import IndexView, RecipeListView, RecipeDetailView, IngredientCreateView, IngredientListView, \
    IngredientUpdateView, LoginFormView

urlpatterns = [
]

urlpatterns += i18n_patterns(
    path("jsi18n/", JavaScriptCatalog.as_view(), name="javascript-catalog"),
    path("admin/", admin.site.urls),
    path('', IndexView.as_view(), name="index"),
    path('recipes', RecipeListView.as_view(), name="recipe_list"),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name="recipe_detail"),
    path('ingredients', IngredientListView.as_view(), name="ingredient_list"),
    path('ingredient/create', IngredientCreateView.as_view(), name="ingredient_create"),
    path('ingredient/update/<int:pk>', IngredientUpdateView.as_view(), name="ingredient_update"),
    path('login', LoginFormView.as_view(), name="login")
)
