import math
from pyexpat.errors import messages
import random
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.urls import reverse
from SchoolProject import settings
from Teacher.models import Course_materials, tbl_Assignment
from .models import  Course, Student_detail, Subject, tbl_Subjetfeedback, tbl_login
from django.contrib import messages

from Schoolapp.models import tbl_login

# Create your views here.
def Home(request):
    request.session['email'] = 'null'
    request.session['password'] = 'null'

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("pass")
        if tbl_login.objects.filter(email=email, password=password).exists():
            request.session['email'] = email
            request.session['password'] = password
            user=tbl_login.objects.get(email=email)
            type=user.type
            if user.type =="Student" or user.type=="student" :
               return redirect('Student')
            elif user.type=="teacher" or type=="Teacher":
                messages.success(request, '----Login Successfull----')        
                return redirect('Teachersindex')
            elif user.type=="parent":
                return redirect('parent')
            else:
                return redirect('home')
    messages.success(request, '----Welcome to St.Sebastine School----')        
    return render(request, "index/index.html")


def About(request):
    return render(request, "index/about.html")


def Courses(request):
    obj=Course.objects.all()
    return render(request, "Courses/courses.html",{'result':obj})



def Teacher(request):
    return render(request, "Teacher/teachers.html")

def Parent(request):
    return render(request, "Parent/Parentindex.html")

def Student(request):
    if 'email' in request.session:
        email=request.session['email']
        data={'email':email}
        return render(request, "Student/Studentindex.html",data)
    else:
        return redirect(Student)


def Studentdetails(request):
    if 'email' in request.session:
        email=request.session['email']
        data={'email':email}
        if request.method == 'POST':
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            hname = request.POST.get('hname')
            father = request.POST.get('father')
            occupation = request.POST.get('occupation')
            pmobile = request.POST.get('pmobile')
            # email = request.POST.get('email')
            profile_pic = request.FILES.get('profile_pic')
            dob = request.POST.get('dob')
            religion = request.POST.get('religion')
            pschool = request.POST.get('pschool')
            mark_obtained = request.POST.get('mark_obtained')
            gender = request.POST.get('gender')
            gname = request.POST.get('gname')
            gmobile = request.POST.get('gmobile')
            gemail = request.POST.get('gemail')
            
            Student_detail.objects.create(fname=fname, lname=lname, hname=hname, father=father, occupation=occupation, pmobile=pmobile, profile_pic=profile_pic,
                            dob=dob, religion=religion, pschool=pschool, mark_obtained=mark_obtained,
                            gender=gender, gname=gname, gmobile=gmobile,gemail=gemail).save()
        else:
            return render(request, "Student/StudentDetails.html",data)
    else:
        return redirect(Student)


def Forgotpsswd(request):
    if request.method == "POST":
        email = request.POST.get("user_email")
        request.session['email'] = email
        # print(email)
        return redirect('reset_psswd')
    return render(request, "index/forgotpsswd.html")


def Resetpsswd(request):
    npsswd=request.POST.get("npsswd")
    email=request.session['email']
    digits="0123456789"
    token = ""
    for i in range(6):
        token += digits[math.floor(random.random() * 10)]

    subject = " St.Sebastine's Higher Secondary School Forgot Password"
    from_email = settings.EMAIL_HOST_USER
    recepient_list = [email]
    htmlgen = "The OTP for changing the password for your account is: " + token + ''
    send_mail(subject, htmlgen, from_email, recepient_list)



    content={
        'token':token
    }
    if request.method == "POST":
        usr=tbl_login.objects.get(email=email)
        usr.password=npsswd
        usr.save()
        return redirect("/")
    return render(request,"index/reset_psswd.html",content)





def Sprofile(request):
    if 'email' in request.session:
        email=request.session['email']
        data=Student_detail.objects.all()
        context={
            "data":data,
            "email":email
                }
        return render(request, "Student/Studentprofile.html",context)
    else:
        return redirect(Student)


def SubjectFeedback(request):
    if 'email' in request.session:
            email=request.session['email']
            department = tbl_login.objects.filter(email=email)
            course=tbl_login.objects.all()
            subject=Subject.objects.all()
            if request.method == 'POST':
                subject = request.POST.get('subject');
                feedback = request.POST.get('feedback');
            tbl_Subjetfeedback.objects.create(subject=subject,feedback=feedback).save()
            return redirect('SubjectFeedback')       
    else:
        return redirect(Student)


def logout_view(request):
    logout(request)
    return redirect('/')

from django.db.models import Q

def searchbar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            multiple_q = Q(Q(Course_name__icontains=query) | Q( Description__icontains=query))
            products = Course.objects.filter(multiple_q) 
            return render(request, 'index/searchbar.html', {'product':products})
        else:
            messages.info(request, 'No search result!!!')
            print("No information to show")
    return render(request, 'index/searchbar.html', {})



def Assgnmnt_View(request):
    if 'email' in request.session:
        email=request.session['email']
        data=tbl_Assignment.objects.all()
        context = {
            'data': data,
            'email':email
        }
        return render(request, 'Student/view_assignment.html', context)
    else:
        return redirect(Home)




def Course_materilals_view(request):
    if 'email' in request.session:
        email=request.session['email']
        data=Course_materials.objects.all()
        context = {
            'data': data,
            'email': email
        }
        return render(request, 'Student/CourseMaterials.html', context)
    else:
        return redirect(Home)



# For Pdf Download
from django.http import FileResponse
from django.shortcuts import get_object_or_404



def download_pdf(request, id):
    pdf_file = get_object_or_404(tbl_Assignment, assignment_id=id)
    return FileResponse(pdf_file.qpaper, as_attachment=True)



def download_pdf_CM(request, id):
    pdf_file = get_object_or_404(Course_materials, id=id)
    return FileResponse(pdf_file.c_materials, as_attachment=True)






