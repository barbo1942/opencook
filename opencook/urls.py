"""opencook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from mainapp.views import get_index,add,add_render,index,signup,signup_post,logout_post,login_post
from recipeapp.views import recipe_api,recipe_create,recipe_post,recipe_show,recipe_update,recipe_update_post,recipe_delete


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$',get_index),
    url(r'^add/(\d+)/(\d+)$',add),
    url(r'^add/$',add_render),
    url(r'^$',index),
    url(r'^signup/$',signup),
    url(r'^signup/post$',signup_post),
    url(r'^logout/post$',logout_post),
    url(r'^login/post$',login_post),
    url(r'^recipe/api$',recipe_api),
    url(r'^recipe/create$',recipe_create),
    url(r'^recipe/post$',recipe_post),
    url(r'^recipe/(\d+)$',recipe_show),
    url(r'^recipe/update/(\d+)$',recipe_update),
    url(r'^recipe/update/post/(\d+)$',recipe_update_post),
    url(r'^recipe/delete/(\d+)$',recipe_delete)
]
