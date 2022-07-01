from asyncio import mixins
from django.shortcuts import render
from .serializers import Stuserializer
from .models import Stumodel
from rest_framework .views import APIView
from rest_framework .response import Response
from rest_framework import mixins,generics
# Create your views here.

class Stu_list_mixins(mixins.ListModelMixin,generics.GenericAPIView):
    queryset = Stumodel.objects.all()
    serializer_class = Stuserializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
class Detail_mixins(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.CreateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Stumodel.objects.all()
    serializer_class = Stuserializer
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
        