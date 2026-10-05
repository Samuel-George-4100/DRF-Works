from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from employees.models import Employee
from django.views import View
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from employees.serializers import EmployeeSerializer


# Create your views here.

#APIView for Reading All employee Records
class EmployeeList(APIView):

    def get(self,request):

        qs=Employee.objects.all()
        #reads all employee records from Employee Table(qs)
        #Employee.objects.all()
        #Employee.objects.get(condition)
        #Employee.objects.filter(condition)

        serializer_instance=EmployeeSerializer(qs,many=True)
        #EmployeeSerializer converts qs into python natives
        #qs contains more than one record so we use many=True

        return Response(serializer_instance.data)
        #sends python native data as json using response class

#API view for creating a new employee record
class EmployeeCreate(APIView):

    def post(self,request):
        #View receives data as request.data
        #calls serializer class for deserialization. Here we pass request.data as argument
        #after validation serializer saves data as model object inside db table
        serializer_instance = EmployeeSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

        #data=json.loads(request.body)
        # data = request.data
        # e=data['empid']
        # n=data['name']
        # a=data['age']
        # p=data['place']
        # g=data['gender']
        # j=data['joining_date']
        # s=data['salary']
        # d=data['designation']
        # c=Employee.objects.create(empid=e,name=n,age=a,place=p,gender=g,joining_date=j,salary=s,designation=d)
        # c.save()
        # return Response({"Message":"Employee Created"})

#APIView for Reading a specific records
class EmployeeDetail(APIView):

    def get(self,request,i):

        #Reads employee object from model
        #qs=Employee.objects.get(id=i)
        e=get_object_or_404(Employee,id=i)

        #converts model object into python native using  EmployeeSerializer
        serializer_instance=EmployeeSerializer(e)

        #sends the response as json us
        return Response(serializer_instance.data)


class EmployeeRetrieve(APIView):
    def get(self,request,id):
        e=list(Employee.objects.filter(id=id).values())
        if e:
            return Response(e,safe=False)
        else:
            return Response({"Message":"Employee not found"})

class EmployeeFullUpdate(APIView):
    def put(self,request,id):
        data=request.data
        try:
            obj=Employee.objects.get(id=id)
            obj.name=data['name']
            obj.age=data['age']
            obj.place=data['place']
            obj.gender=data['gender']
            obj.joining_date=data['joining_date']
            obj.salary=data['salary']
            obj.designation=data['designation']
            obj.save()
            return Response({"Message":"Employee Updated"})
        except:
            return Response({"Message":"Employee not found"})

# class EmployeePartialUpdate(APIView):
#     def patch(self,request,id):
#         data=request.data
#         try:
#             obj=Employee.objects.get(id=id)
#             if 'empid' in data:
#                 obj.empid=data['empid']
#             if 'name' in data:
#                 obj.name=data['name']
#             if 'age' in data:
#                 obj.age=data['age']
#             if 'place' in data:
#                 obj.place=data['place']
#             if 'gender' in data:
#                 obj.gender=data['gender']
#             if 'joining_date' in data:
#                 obj.joining_date=data['joining_date']
#             if 'salary' in data:
#                 obj.salary=data['salary']
#             if 'designation' in data:
#                 obj.designation=data['designation']
#             return Response({"Message":"Employee Partially Updated"})
#         except:
#             return Response({"Message":"Employee not found"})


#API View for deleting a specific record

class EmployeeDelete(APIView):

    def delete(self,request,i):
        e=get_object_or_404(Employee,id=i)
        e.delete()
        return Response({"Message":"Employee deleted"})

#API View for updating an existing record(Full updation)
class EmployeeUpdate(APIView):

    def put(self,request,i):
        e=Employee.objects.get(id=i)
        serializer_instance=EmployeeSerializer(e,request.data)
        if serializer_instance.is_valid():
            serializer_instance.save() #calls update() inside serializer class
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

class EmployeePartialUpdate(APIView):

    def patch(self,request,i):
        e=get_object_or_404(Employee,id=i)
        serializer_instance=EmployeeSerializer(e,request.data,partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)