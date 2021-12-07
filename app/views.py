from django.views.generic import TemplateView, ListView, DetailView

from app.models import Recipe


class IndexView(TemplateView):
    template_name = "index.html"

class RecipeListView(ListView):
    template_name = "recipe_list.html"
    model = Recipe

class RecipeDetailView(DetailView):
    template_name = "recipe_detail.html"
    model = Recipe