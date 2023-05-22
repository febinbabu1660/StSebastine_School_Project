# Create your views here.


import csv
from datetime import datetime
from django.shortcuts import redirect, render
from Schoolapp.models import Class_teachers, Course, Subject, tbl_login
from Schoolapp.views import Home
import Teacher
from Teacher.models import Mark
from django.contrib import messages



def Teachersindex(request):
    if 'email' in request.session:
        email=request.session['email']
        teacher=tbl_login.objects.filter(email=email)
        data={'email':email,
              'teacher':teacher}
        return render(request, "Teacher/Teacherindex.html",data)

    else:
        return redirect(Home)


def viewClass(request):
    if 'email' in request.session:
        email=request.session['email']
        course=Class_teachers.objects.filter(class_teacher_id=email)
        if course:
            course=Class_teachers.objects.get(class_teacher_id=email)
            stream=course.Course_name
            student=tbl_login.objects.filter(department=stream,type='Student')
            data={'email':email,
                'student':student}
            return render(request, "Teacher/view_class.html",data)
        else:
            messages.success(request, '----You have no class assigned ----')        
            return redirect(Teacher)

    else:
        return redirect(Teacher)


def Assignment(request):
        if 'email' in request.session:
            email=request.session['email']
            course=Course.objects.all()
            subject=Subject.objects.all()
            if request.method == 'POST':
                Course_name = request.POST.get('Course_name');
                subject_name = request.POST.get('subject_name');
                topic = request.POST.get('topic');
                start_date = request.POST.get('start_date');
                submission_date = request.POST.get('submission_date');
                qpaper = request.FILES.get('qpaper');
                # leaveRecords = request.POST['proof']
                email = request.user
                tbl_Assignment.objects.create(Course_name_id=Course_name,subject_name_id=subject_name,topic=topic,start_date=start_date, submission_date=submission_date, qpaper=qpaper).save()
                return redirect('Assignment')
            data={'course':course,'subject':subject,'email':email}
            return render(request, 'Teacher/assgnmt_upld.html',data)
        else:
            return redirect(Teacher)




def Course_material(request):
        if 'email' in request.session:
            email=request.session['email']
            course=Course.objects.all()
            subject=Subject.objects.all()
            if request.method == 'POST':
                Course_name = request.POST.get('Course_name');
                subject_name = request.POST.get('subject_name');
                Note = request.POST.get('Note');
                upload_date = request.POST.get('upload_date');
                c_materials = request.FILES.get('c_materials');
                # leaveRecords = request.POST['proof']
                email = request.user
                Course_materials.objects.create(Course_name_id=Course_name,subject_name_id=subject_name,Note=Note,upload_date=upload_date, c_materials=c_materials).save()
                return redirect('Course_materials')
            data={'course':course,'subject':subject,'email':email}
            return render(request, 'Teacher/course_materials.html',data)
        else:
            return redirect(Teacher)





def Attendence(request):
    if 'email' in request.session:
        email=request.session['email']
        data={'email':email}
        return render(request, "Teacher/attendence.html",data)

    else:
        return redirect(Home)




def Mark1(request):
    if 'email' in request.session:
        email=request.session['email']
        data={'email':email}
        return render(request, "Teacher/result.html",data)

    else:
        return redirect(Home)



import csv

def upload_marks(request):
    if request.method == "POST":
        csv_file = request.FILES["csv_file"]
        if not csv_file.name.endswith('.csv'):
            messages.warning(request, 'The uploaded file is not a CSV file.')
            return redirect('upload_marks')

        # Decode the CSV file data and split it into rows
        # csv_data = csv.reader(csv_file.read().decode("utf-8").splitlines())
        csv_data = csv_file.read().decode("utf-8").splitlines()

        

        # Skip the header row
        # next(csv_data)

        # Iterate through each row and create Mark objects
        for row in csv_data:
            row_data = row.split(",")
            if len(row_data) != 8:  # Assuming each row has 8 columns
                messages.warning(request, 'Invalid data in CSV file.')
                return redirect('upload_marks')

            name, course_name, subject1_marks, subject2_marks, subject3_marks, subject4_marks, subject5_marks, subject6_marks= row_data
            
            
            try:
                # Convert marks to integers
                subject1_marks = int(subject1_marks)
                subject2_marks = int(subject2_marks)
                subject3_marks = int(subject3_marks)
                subject4_marks = int(subject4_marks)
                subject5_marks = int(subject5_marks)
                subject6_marks = int(subject6_marks)
            except ValueError:
                messages.warning(request, 'Invalid data in CSV file.')
                return redirect('upload_marks')
            # Create a new Mark object
            Mark.objects.create(name=name, course_name=course_name, subject1_marks=subject1_marks, 
                            subject2_marks=subject2_marks, subject3_marks=subject3_marks, 
                            subject4_marks=subject4_marks, subject5_marks=subject5_marks,
                            subject6_marks=subject6_marks).save()
            

        messages.success(request, 'File uploaded successfully.')
        return redirect('upload_marks')

    return render(request, 'Teacher/upload_marks.html')






# for downloading the data 
    
from django.http import HttpResponse

from .models import Course_materials, tbl_Assignment

def download_data(request):
    if 'email' in request.session:
        email=request.session['email']
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="students.csv"'

        writer = csv.writer(response)
        writer.writerow(['First Name','Last Name', 'Email'])  # Add header row

        course=Class_teachers.objects.filter(class_teacher_id=email)
        if course:
            course=Class_teachers.objects.get(class_teacher_id=email)
            stream=course.Course_name
            # student=tbl_login.objects.filter(department=stream,type='Student')

            queryset = tbl_login.objects.filter(department=stream,type='Student')  # Replace with your own queryset
            for obj in queryset:
                writer.writerow([obj.fname, obj.lname, obj.email])  # Replace with your own field names

            return response

        else:
            return redirect(Teacher)
    else:
        return redirect(Teacher)