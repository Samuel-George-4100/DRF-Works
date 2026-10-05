from rest_framework import serializers

from recipeapi.recipeapp.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):

    recipe_name = serializers.CharField()
    meal_type = serializers.CharField()
    cuisine = serializers.CharField()
    ingredients = serializers.TextField()
    instructions = serializers.TextField()
    image = serializers.ImageField()