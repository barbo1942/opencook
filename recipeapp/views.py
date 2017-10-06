from django.shortcuts import render, redirect

# Create your views here.
from .models import Recipe
from django.http import JsonResponse
from django.core import serializers

from django import forms
from django.contrib import messages

class RecipeForm(forms.ModelForm):
  class Meta:
    model =Recipe
    fields=['title','image_path','description']

def recipe_api(request):
  recipes=Recipe.objects.all()
  data= serializers.serialize('json',recipes)
  return JsonResponse({'data': data})


def recipe_create(request):
  return render(request,'recipe_create.html')

def recipe_post(request):
  if request.method=='POST':
    form =RecipeForm(request.POST)
    if form.is_valid():
      new_recipe= form.save()
      # print(new_recipe)
      messages.add_message(request,messages.SUCCESS,'分享成功！')
      return redirect('/')
    else:
      messages.add_message(request,messages.ERROR,'分享失敗，請再輸入一次')
      return redirect('/recipe/create')

def recipe_show(request,recipe_id):
  recipe= Recipe.objects.get(pk=recipe_id)
  # print(recipe.title)
  return render(request,'recipe.html',locals())

def recipe_update(request,recipe_id):
  recipe= Recipe.objects.get(pk=recipe_id)
  return render(request,'recipe_update.html',locals())


def recipe_update_post(request,recipe_id):
  if request.method=='POST':
    form =RecipeForm(request.POST)
    title=request.POST['title']
    description=request.POST['description']
    image_path=request.POST['image_path']
    if form.is_valid():
      recipe= Recipe.objects.filter(pk=recipe_id)
      recipe.update(title=title)
      recipe.update(description=description)
      recipe.update(image_path=image_path)
      print("更新菜品",recipe[0].title,recipe[0].description,recipe[0].image_path)
      messages.add_message(request,messages.SUCCESS,'更新成功！')
      return redirect('/recipe/'+recipe_id)
    else:
      messages.add_message(request,messages.ERROR,'更新失敗，請再輸入一次')
      return redirect('/recipe/recipe_id')

def recipe_delete(request,recipe_id):
  Recipe.objects.filter(pk=recipe_id).delete()
  recipe= Recipe.objects.all()
  messages.add_message(request,messages.SUCCESS,'刪除成功！')
  return render(request,'index.html',locals())
  