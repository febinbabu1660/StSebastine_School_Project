from django.shortcuts import render
from django.shortcuts import redirect

from Leave.models import leaveModel, tbl_teacherleave
from Schoolapp.models import tbl_login
from Schoolapp.views import Home


# Create your views here.


def leave(request):
    if 'email' in request.session:
        email=request.session['email']
        data=leaveModel.objects.filter(email=email)
        context = {
            'data': data
        }
        return render(request, 'Leave/leave_view.html', context)
    else:
        return redirect(Home)

def leaveApply(request):
    if 'email' in request.session:
        email=request.session['email']
        user=tbl_login.objects.get(email=email)
        if request.method == 'POST':
            # print('1')
            name = request.POST['name']
            leaveDate = request.POST['date']
            leaveDiv = request.POST['session']
            leaveReason = request.POST['reason']
            # leaveRecords = request.POST['proof']
            # print(leaveDate)
            if leaveDiv=='FD':
                leaveDiv='AN, FN'
            leaveStatus = False
            email = request.user
            leaveModel.objects.create(name=name,email=user, leaveDate=leaveDate, leaveDiv=leaveDiv, leaveReason=leaveReason, leaveStatus=leaveStatus).save()
            return redirect('leave')
        return render(request, 'Leave/leave.html')
    else:
        return redirect(Home)




# for teacher leave
def teacherleave(request):
    if 'email' in request.session:
        user=request.session['email']
        if request.method=='POST':
            date=request.POST.getlist('apply_date')
            for i in date:
                reason=request.POST.getlist('reason_'+i)
                for j in reason:
                    type=request.POST.getlist('type_'+i)
                    for k in type:
                        session=request.POST.getlist('session_'+i)
                        for l in session:
                            tbl_teacherleave(teacher_id=user,leaveDate=i,leaveType=k,leaveSession=l,leaveReason=j).save()
            return redirect(leave)
        return render(request, 'Leave/teacher_leave.html')
    else:
        return redirect(Home)
    


def teacherleaveView(request):
    if 'email' in request.session:
        email=request.session['email']
        data=tbl_teacherleave.objects.filter(teacher_id=email)
        context = {
            'data': data
        }
        return render(request, 'Leave/teacher_leaveView.html', context)
    else:
        return redirect(Home)