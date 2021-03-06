from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, FormView

from app.forms.login import LoginForm
from app.models import Recipe, Ingredient


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['title'] = "Titre de ma page"
        return result


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


class LoginFormView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = "/"

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            messages.add_message(
                self.request, messages.INFO,
                f'Hello {user.username}'
            )
            return super().form_valid(form)

        form.add_error(None, "email / mdp invalide")
        return super().form_invalid(form)


class TestJsonView(View):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        ingredients = Ingredient.objects.all()
        return JsonResponse(
            [{"id": i.pk,
              "name": i.name_singular
            } for i in ingredients],
            safe=False
        )
