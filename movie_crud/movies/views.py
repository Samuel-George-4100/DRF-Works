from django.shortcuts import render
from rest_framework.views import APIView
from movies.models import Movie
from movies.serializers import MovieSerializer,UserSerializer
from rest_framework.response import Response
from rest_framework import status,viewsets
from django.shortcuts import get_object_or_404
from django.db.models import Q
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


# class MovieListCreate(APIView):
#
#     def get(self,request):
#         m=Movie.objects.all()
#         serializer_instance=MovieSerializer(m,many=True)
#         return Response(serializer_instance.data,status=status.HTTP_200_OK)
#
#     def post(self, request):
#         client_data=request.data
#         serializer_instance=MovieSerializer(data=client_data)
#         if serializer_instance.is_valid():
#             #cleaned_data=serializer_instance.validated_data
#             #title=cleaned_data['title']
#             serializer_instance.save()
#             return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)



#API View for reading a specific record
#API View for updating a specific record
#API View for deleting a specific record

"""Using mixins class"""
from rest_framework import mixins,generics

# class MovieListCreate(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset=Movie.objects.all()
#     serializer_class=MovieSerializer
#     def get(self,request):
#         return self.list(request)
#
#     def post(self,request):
#         return self.create(request)
#
#
# class MovieRetrieveUpdateDelete(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset=Movie.objects.all()
#     serializer_class=MovieSerializer

    # def get(self,request,pk):
    #     return self.retrieve(request,pk)
    #
    # def put(self,request,pk):
    #     return self.update(request,pk)
    #
    # def delete(self,request,pk):
    #     return self.destroy(request,pk)
# class MovieRetrieveUpdateDelete(APIView):
#
#     def get(self,request,id):
#         model_object=get_object_or_404(Movie,id=id)
#         serializer_instance=MovieSerializer(model_object)
#         return Response(serializer_instance.data,status=status.HTTP_200_OK)
#
#     def put(self,request,id):
#         form_data=request.data
#         model_object=Movie.objects.get(id=id)#reads movie instance
#         serializer_instance=MovieSerializer(model_object,form_data)
#         if serializer_instance.is_valid():
#             serializer_instance.save()
#             return Response(serializer_instance.data,status=status.HTTP_200_OK)
#
#     def patch(self,request,id):
#         form_data=request.data
#         model_object=get_object_or_404(Movie,id=id)
#         serializer_instance=MovieSerializer(model_object,form_data,partial=True)
#         if serializer_instance.is_valid():
#             serializer_instance.save()
#             return Response(serializer_instance.data,status=status.HTTP_200_OK)
#
#     def delete(self,request,id):
#         model_object=get_object_or_404(Movie,id=id)
#         model_object.delete()
#         return Response({"message":"deleted"},status=status.HTTP_204_NO_CONTENT)

"""Using generics class"""


# class MovieListCreate(generics.ListCreateAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#
# class MovieRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer


"""Viewsets"""

class MovieView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

#Search API View

# class SearchAPIView(APIView):
#     def get(self,request):
#
#         #fetches data coming from request url
#         data = self.request.query_params.get('search')
#
#         #filters movie records having title matching with data
#         m = Movie.objects.filter(Q(title__icontains=data)|
#                                  Q(director__icontains=data)|
#                                  Q(language__icontains=data))
#
#         if not m.exists():
#             return Response({'message':'No records found'}, status=status.HTTP_200_OK)
#
#         #converts the qs into native using serializer class
#         serializer_instance = MovieSerializer(m,many=True)
#
#         #returns response as json using Response class
#         return Response(serializer_instance.data,status=status.HTTP_200_OK)


from rest_framework.filters import SearchFilter

class SearchAPIView(APIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends=[SearchFilter]
    search_fields=['title','director','language']

class RegisterAPIView(APIView):
    def post(self,request):
        form_data=request.data
        serializer_instance=UserSerializer(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)