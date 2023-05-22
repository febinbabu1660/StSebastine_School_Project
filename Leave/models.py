from django.db import models

from Schoolapp.models import tbl_login

# Create your models here.

class leaveModel(models.Model):
    leave_choices = (
        ('FN', 'FN'),
        ('AN', 'AN'),
        ('FD', 'FD'),
        ('None', 'None'),
    )
    leaveId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.ForeignKey(tbl_login, on_delete=models.CASCADE)
    leaveDate = models.DateField()
    leaveDiv = models.CharField(max_length=10)
    leaveReason = models.CharField(max_length=50)
    leaveStatus = models.BooleanField('Approved', default=False)
    # type = models.ForeignKey(tbl_login, on_delete=models.CASCADE)
    # leaveRecords = models.FileField(upload_to="media/leave/")

    def __str__(self):
        return self.email.email
    


# for teacher leave
class tbl_teacherleave(models.Model):
    teacher = models.ForeignKey(tbl_login, on_delete=models.CASCADE)
    leaveDate = models.CharField(null=True,max_length=50)
    leaveType = models.CharField(max_length=10,null=True)
    leaveReason = models.CharField(max_length=50,null=True)
    leaveSession = models.CharField(max_length=50,null=True)
    leaveStatus = models.BooleanField('Approved', default=False)

 

