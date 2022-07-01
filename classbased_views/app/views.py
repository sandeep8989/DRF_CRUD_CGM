from django.shortcuts import render
from .serializers import Empserializers
from .models import Empmodel
from rest_framework .views import APIView
from rest_framework .response import Response
from rest_framework import status

# Create your views here.

class Employee(APIView):
    def get(self,request):
        task = Empmodel.objects.all()
        serializer = Empserializers(task,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = Empserializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class Employee1(APIView):
    def get(self,request,pk):
        task = Empmodel.objects.get(pk=pk)
        serializer = Empserializers(task,many=False)
        return Response(serializer.data)
    
    def put(self,request,pk):
        task = Empmodel.objects.get(pk=pk)
        serializer = Empserializers(data = request.data,instance = task)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        task = Empmodel.objects.get(pk=pk)
        task.delete()
        return Response("Deleted Successfully")