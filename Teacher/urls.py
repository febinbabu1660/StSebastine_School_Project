from . import views
from django.urls import path


urlpatterns = [
    # path('tlogin/', views.Tlogin, name='tlogin'),
    # path('teacher_reg/', views.Teacher_reg, name='teacher_reg'),
     path('Teachersindex/', views.Teachersindex, name='Teachersindex'),
     path('Assignment/', views.Assignment, name='Assignment'),
     path('Attendence/', views.Attendence, name='Attendence'),
     path('Mark/', views.Mark1, name='Mark'),
     path('upload_marks/', views.upload_marks, name='upload_marks'),
     path('Course_materials/', views.Course_material, name='Course_materials'),
     path('viewClass/', views.viewClass, name='viewClass'),
     path('download_data/', views.download_data, name='download_data'),
  
]
