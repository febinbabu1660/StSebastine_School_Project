from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.leave, name='leave'),
    path('apply', views.leaveApply, name='leaveApply'),
    path('teacherleave', views.teacherleave, name='teacherleave'),
    path('teacherleaveView', views.teacherleaveView, name='teacherleaveView'),
    ]