from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import EmployeeSerializer
from .models import Employee

from django.shortcuts import render

# Create your views here.
from typing import Any

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from myapi.models import Employee


class EmployeeViewSet( viewsets.ModelViewSet ):
    queryset = Employee.objects.all().order_by( 'id' )
    serializer_class = EmployeeSerializer


"""
def insert(request):  # HTTPRequest / HTTPResponse
    inserted = Employee.objects.all() 
    


def update(request, id):  # HTTPRequest / HTTPResponse
    updated = Employee.objects.get(pk=id)
"""


def getemployees(request):
    employee_list = Employee.objects.all()
    return render( request, 'myapi/getemployees_all.html', {'employee_list': employee_list} )


"""

def getemployee(request, id):
    display_one = Employee.objects.all()
    return render( request, 'myapi/getemployee.html', {'display_one': display_one})

"""


class DeleteTodoAPIView(APIView):
    def get(self,request,pk):
        todo = Employee.objects.get(id=pk)
        todo_instance = Employee.objects.get(id=pk)
        todo_instance.delete()
        return Response('Deleted')
