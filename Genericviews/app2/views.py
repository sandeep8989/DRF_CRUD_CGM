
from django.shortcuts import render
from .serializers import Workerserializer, serializers
from .models import Workermodel
from rest_framework .views import APIView
from rest_framework .response import Response
from rest_framework import generics

# Create your views here.

class Worker_Create_Generics(generics.CreateAPIView):
    queryset = Workermodel.objects.all()
    serializer_class = Workerserializer

class Worker_List_Generics(generics.ListAPIView):
    queryset = Workermodel.objects.all()
    serializer_class = Workerserializer

class Worker_Detail_Generics(generics.RetrieveAPIView,
                              generics.UpdateAPIView,
                              generics.DestroyAPIView):
    queryset = Workermodel.objects.all()
    serializer_class = Workerserializer

class Worker_List_Create_Generics(generics.ListCreateAPIView):
    queryset = Workermodel.objects.all()
    serializer_class = Workerserializer

class Worker_All_Generics(generics.RetrieveUpdateDestroyAPIView):
    queryset = Workermodel.objects.all()
    serializer_class = Workerserializer
