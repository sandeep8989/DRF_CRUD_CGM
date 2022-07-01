from django.contrib import admin
from app.models import Empmodel
# Register your models here.

@admin.register(Empmodel)
class Empadmin(admin.ModelAdmin):
    list_display = ['empid','name','age','Address']