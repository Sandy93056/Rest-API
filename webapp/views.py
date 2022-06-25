from django.shortcuts import render
from django.http import HttpResponse
from .models import employees

from .serializers import employeesSerializer

from rest_framework.views import APIView



# Create your views here.

class employeeList(APIView):

    def get(self, request):
        employess1 = employees.objects.all()
        serializer = employeesSerializer(employess1, many=True)

        return HttpResponse(serializer.data)

    def post(self):
        pass


    