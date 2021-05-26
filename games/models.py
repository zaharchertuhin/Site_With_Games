from django.db import models
from django.contrib.auth import get_user_model

class Game(models.Model):
    title = models.CharField(max_length=50)
    discription = models.TextField()
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True)
    slug = models.SlugField(unique=True)