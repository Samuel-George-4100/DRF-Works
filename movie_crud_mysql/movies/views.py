from django.shortcuts import render
from rest_framework.views import APIView
from movies.models import Movie
from movies.serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
# Create your views here.

#API View for reading all movie records

# class MovieList(APIView):
#
#     def get(self,request):
#         m=Movie.objects.all()
#         serializer_instance=MovieSerializer(m,many=True)
#         return Response(serializer_instance.data)

#API View for creating a new record

# class MovieCreate(APIView):
#
#     def post(self,request):
#         client_data=request.data
#         serializer_instance=MovieSerializer(data=client_data)
#         if serializer_instance.is_valid():
#             #cleaned_data=serializer_instance.validated_data
#             #title=cleaned_data['title']
#             serializer_instance.save()
#             return Response(serializer_instance.data)
#         else:
#             return Response(serializer_instance.errors)


class MovieListCreate(APIView):

    def get(self,request):
        m=Movie.objects.all()
        serializer_instance=MovieSerializer(m,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

    def post(self, request):
        client_data=request.data
        serializer_instance=MovieSerializer(data=client_data)
        if serializer_instance.is_valid():
            #cleaned_data=serializer_instance.validated_data
            #title=cleaned_data['title']
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

#API View for reading a specific record
#API View for updating a specific record
#API View for deleting a specific record

class MovieRetrieveUpdateDelete(APIView):

    def get(self,request,id):
        model_object=get_object_or_404(Movie,id=id)
        serializer_instance=MovieSerializer(model_object)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

    def put(self,request,id):
        form_data=request.data
        model_object=Movie.objects.get(id=id)#reads movie instance
        serializer_instance=MovieSerializer(model_object,form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_200_OK)

    def patch(self,request,id):
        form_data=request.data
        model_object=get_object_or_404(Movie,id=id)
        serializer_instance=MovieSerializer(model_object,form_data,partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_200_OK)

    def delete(self,request,id):
        model_object=get_object_or_404(Movie,id=id)
        model_object.delete()
        return Response({"message":"deleted"},status=status.HTTP_204_NO_CONTENT)
