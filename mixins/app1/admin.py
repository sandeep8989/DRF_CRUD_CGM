from django.contrib import admin
from app1.models import Stumodel

# Register your models here.
@admin.register(Stumodel)
class Stuadmin(admin.ModelAdmin):
    list_display = ['stuid','name','age','address']