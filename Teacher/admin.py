from django.contrib import admin
from Teacher.models import Course_materials, Mark, tbl_Assignment
from django.urls import path
from django.shortcuts import render
# Register your models here.



admin.site.register(tbl_Assignment)
admin.site.register(Mark)
admin.site.register(Course_materials)