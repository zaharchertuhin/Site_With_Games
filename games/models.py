from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Game(models.Model):
    title = models.CharField(max_length=50)
    discription = models.TextField()
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True)
    # def Get_absolute_url(self):
    #     return reverse("game_detail", args=[self.slug])

class Registry(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)