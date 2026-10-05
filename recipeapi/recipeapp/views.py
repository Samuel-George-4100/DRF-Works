from django.shortcuts import render
from rest_framework.views import APIView
from recipeapp.serializers import RecipeSerializer


# Create your views here.

class CreateRecipe(APIView):
    def post(self, request):
        client_data = request.data
        serializer_obj = RecipeSerializer(data=client_data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response()