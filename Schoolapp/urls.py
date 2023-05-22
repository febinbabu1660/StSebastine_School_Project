from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home, name='home'),
    # path('register/', views.register, name='register'),
    # # path('login/', views.login, name='login'),
    # path('login/', views.Login, name='login'),
    path('Teacher/', views.Teacher, name='Teacher'),
    path('about/', views.About, name='about'),
    path('courses/', views.Courses, name='courses'),
    # path('students_data/',views.student_upload,name="student_data"),
    path('Student/', views.Student, name='Student'),
    path('Studentdetails/', views.Studentdetails, name='Studentdetails'),
    path('SubjectFeedback/', views.SubjectFeedback, name='SubjectFeedback'),
    path('parent/', views.Parent, name='parent'),
    path('Sprofile/', views.Sprofile, name='Sprofile'),
    path('Assgnmnt_View/', views.Assgnmnt_View, name='Assgnmnt_View'),
    path('Course_materilals_view/', views.Course_materilals_view, name='Course_materilals_view'),
    # path('HScience/', views.HScience, name='HScience'),
    # path('Commerece/', views.Commerece, name='Commerece'),
    # path('Humanities/', views.Humanities, name='Humanities'),
    path('Forgotpsswd/', views.Forgotpsswd, name='forgotpsswd'),
    path('Resetpsswd/', views.Resetpsswd, name='reset_psswd'),
    path('logout', views.logout_view , name='logout'),
    path('searchbar/', views.searchbar, name='searchbar'),
    path('download_pdf/<int:id>/', views.download_pdf, name='download_pdf'),
    path('download_pdf_CM/<int:id>/', views.download_pdf_CM, name='download_pdf_CM'),
   

    # path('activate/<uidb64>/<token>/', views.activate, name='activate'),

]
