from pyexpat import model
from tabnanny import verbose
from turtle import title
from django.db import models
from django.forms import CharField

# Create your models here.

class Posts(model.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural='Posts'

    def __str__(self):
        return self.title
