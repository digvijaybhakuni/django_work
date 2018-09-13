from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Employee
from .serializers import EmployeeSerializer

# Create your views here.


class EmployeeSearchAPI(APIView):

    def get(self, request):
        emps = Employee.objects.all()
        empsjs = EmployeeSerializer(emps, many=True)
        return Response(empsjs.data)


class EmployeeCrudApi(ModelViewSet): # generics.ListCreateAPIView
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
