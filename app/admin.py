from django.contrib import admin

# Register your models here.
from app.models import Recipe
from app.models import Tag
from app.models import RecipeTag

admin.site.register(Recipe)
admin.site.register(Tag)
admin.site.register(RecipeTag)
