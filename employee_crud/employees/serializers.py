from rest_framework import serializers

from employees.models import Employee


# Create your models here.

class EmployeeSerializer(serializers.Serializer):
    empid=serializers.IntegerField()
    name=serializers.CharField(max_length=30)
    age=serializers.IntegerField()
    place=serializers.CharField(max_length=30)

    gender_choices=[('male','Male'),('female','Female')]# (dbvalue,displayvalue)

    gender=serializers.ChoiceField(choices=gender_choices)

    joining_date=serializers.DateField()

    #joined_date=models.DateField(auto_now_add=True)#it adds date value automatically
    #joined_date=models.DateTimeField(auto_now_add=True)#it adds time and date value automatically

    salary=serializers.IntegerField()
    designation=serializers.CharField()
    profile_image=serializers.ImageField()



    #After validation and before saving
    def create(self,validated_data):
        e=Employee.objects.create(**validated_data)
        return e #returns model object

    #After validation and before saving
    def update(self,i,validated_data):
        i.empid=validated_data.get('empid',i.empid)
        i.name=validated_data.get('name',i.name)
        i.age=validated_data.get('age',i.age)
        i.place=validated_data.get('place',i.place)
        i.gender=validated_data.get('gender',i.gender)
        i.joining_date=validated_data.get('joining_date',i.joining_date)
        i.salary=validated_data.get('salary',i.salary)
        i.designation=validated_data.get('designation',i.designation)
        i.save()
        return i

    def validate(self,data):
        if data['age']<=0:
            raise serializers.ValidationError('Age must be greater than 0')
        return data