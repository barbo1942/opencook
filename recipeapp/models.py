from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User

class Recipe(models.Model):
  title = models.CharField(max_length = 100)
  image_path = models.CharField(max_length = 500)
  description = models.TextField()
  created_at = models.DateTimeField(default = timezone.now)
  # author = models.ForeignKey(User,null=True, blank=True)
  author= models.CharField(max_length = 20,null=True)

  @property
  def user(self):
      return User.objects.get(author=self.username)

  @user.setter
  def user(self, user):
      if user.is_authenticated():
          self.username = user.username
          print("user.username: ",user.username)
          print("self.username: ",self.username)
      else:
          self.username = '#anonymous'