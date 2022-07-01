from django.contrib import admin
from app2.models import Workermodel

# Register your models here.

@admin.register(Workermodel)
class Workeradmin(admin.ModelAdmin):
    list_display = ['workerid','name','age','address']