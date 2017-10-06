from django.contrib import admin

# Register your models here.
from recipeapp.models import Recipe 
# admin.site.register(Recipe)

class RecipeAdmin(admin.ModelAdmin):
  list_display=('id','title','description','created_at','author','image_path')

admin.site.register(Recipe,RecipeAdmin)