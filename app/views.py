from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView

from app.models import Recipe, Ingredient


class IndexView(TemplateView):
    template_name = "index.html"


class RecipeListView(ListView):
    template_name = "recipe_list.html"
    model = Recipe


class IngredientListView(ListView):
    template_name = "ingredient_list.html"
    model = Ingredient


class RecipeDetailView(LoginRequiredMixin, DetailView):
    template_name = "recipe_detail.html"
    model = Recipe

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['ingredients'] = Ingredient.objects.filter(
            recipeingredientunit__recipe__pk=self.object.pk
        )
        return result


class IngredientCreateView(LoginRequiredMixin, CreateView):
    template_name = "ingredient_create.html"
    model = Ingredient
    fields = ('name_singular', 'name_plural')
    success_url = reverse_lazy('ingredients_list')


class IngredientUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "ingredient_create.html"
    model = Ingredient
    fields = ('name_singular', 'name_plural')
    success_url = reverse_lazy('ingredients_list')
