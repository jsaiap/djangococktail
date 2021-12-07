from django.views.generic import TemplateView, ListView

from app.models import Recipe


class IndexView(TemplateView):
    template_name = "index.html"

class RecipeListView(ListView):
    template_name = "recipe_list.html"
    model = Recipe