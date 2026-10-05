from django.db import models

# Create your models here.
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=30)
    meal_type = models.CharField(max_length=30)
    cuisine = models.CharField(max_length=30)
    ingredients = models.TextField()
    instructions = models.TextField()
    image = models.ImageField(upload_to='media',null=True)