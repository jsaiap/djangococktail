from django.contrib import admin

# Register your models here.
from app.models import Recipe, Tag, RecipeTag, RecipeIngredientUnit, Ingredient, Unit

admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Unit)
admin.site.register(Tag)
admin.site.register(RecipeTag)
admin.site.register(RecipeIngredientUnit)
