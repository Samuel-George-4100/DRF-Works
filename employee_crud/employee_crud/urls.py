"""
URL configuration for employee_crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from employees import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('employeelist',views.EmployeeList.as_view(),name='employeelist'),
    path('employeecreate',views.EmployeeCreate.as_view(),name='employeecreate'),
    path('employeeretrieve/<int:id>',views.EmployeeRetrieve.as_view(),name='employeeretrieve'),
    path('employeefullupdate/<int:id>', views.EmployeeFullUpdate.as_view(), name='employeefullupdate'),
    path('employeepartialupdate/<int:id>', views.EmployeePartialUpdate.as_view(), name='employeepartialupdate'),
    path('employeedetail/<int:i>',views.EmployeeDetail.as_view(),name='employeedetail'),
    path('employeedelete/<int:i>',views.EmployeeDelete.as_view(),name='employeedelete'),
    path('employeeupdate/<int:i>',views.EmployeeUpdate.as_view(),name='employeeupdate'),
    path('employeepartialupdate/<int:i>',views.EmployeePartialUpdate.as_view(),name='employeepartialupdate'),
]
