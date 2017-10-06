from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from recipeapp.models import Recipe
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth



def get_index(request):
  return HttpResponse('hello world')
#收到request 回覆response

def add(request,a,b):
  result=int(a)+int(b)
  return HttpResponse('a+b='+str(result))

def add_render(request):
  return render(request,'add_render.html',{'title': 'oopen cook'})

def index(request):
  recipes = Recipe.objects.all()
  # for recipe in recipes:
    # print(recipe.title+": "+recipe.description+ str(recipe.created_at))
  return render(request,'index.html',locals())
  # title='Open Cook'
  # return render(request,'index.html',{'title': title})

  # set_cookie
  # response= render(request,'index.html',locals())
  # response.set_cookie(key='0929name2',value='0929lalala',expires=datetime.now()+timedelta(days=1))
  # return response

  # session
  # request.session['name_session']=25
  # response= render(request,'index.html',locals())
  # return response

def signup(request):
  # print(request.session['name_session'])
  return render(request,'signup.html')

def signup_post(request):
  username=request.POST['username']
  email=request.POST['email']
  password=request.POST['password']
  # print(username,email,password)
  user = User.objects.create_user(username,email,password)
  if user:
    return redirect('/',locals())
  else:
    return redirect('/signup',locals())

def logout_post(request):
  auth.logout(request)
  return redirect('/')

def login_post(request):
  username=request.POST['username']
  password=request.POST['password']
  user=authenticate(username=username,password=password)
  if user is not None:
    auth.login(request,user)
    return redirect('/',locals())
  else:
    return redirect('/',locals())