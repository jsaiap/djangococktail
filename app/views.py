from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView

from app.models import Recipe, Ingredient


class IndexView(TemplateView):
    template_name = "index.html"


class RecipeListView(ListView):
    template_name = "recipe_list.html"
    model = Recipe


class RecipeDetailView(LoginRequiredMixin, DetailView):
    template_name = "recipe_detail.html"
    model = Recipe

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['ingredients'] = Ingredient.objects.filter(
            recipeingredientunit__recipe__pk=self.object.pk
        )
        return result