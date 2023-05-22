from django.db import models

from Schoolapp.models import Course, Subject
# Create your models here.


class tbl_Assignment(models.Model):
    assignment_id = models.AutoField(primary_key=True)
    Course_name = models.ForeignKey(Course,on_delete=models.CASCADE)
    subject_name = models.ForeignKey(Subject,on_delete=models.CASCADE)
    topic = models.CharField(max_length=100, blank=True, null=True)
    start_date =  models.DateField(auto_now_add=False)
    submission_date =  models.DateField(auto_now_add=False)
    qpaper = models.FileField(upload_to='Assignment/subject', null=True)

    # def __str__(self):
    #     return self.subject_name
    

class Course_materials(models.Model):
    Course_name = models.ForeignKey(Course,on_delete=models.CASCADE)
    subject_name = models.ForeignKey(Subject,on_delete=models.CASCADE)
    Note = models.CharField(max_length=100, blank=True, null=True)
    upload_date =  models.DateField(auto_now_add=True)
    c_materials = models.FileField(upload_to='Course_Materials/subject', null=True)

    def __str__(self):
        return self.Note



class Mark(models.Model):
    # exam_name = models.ForeignKey(Exam_type, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    subject1_marks = models.IntegerField()
    subject2_marks = models.IntegerField()
    subject3_marks = models.IntegerField()
    subject4_marks = models.IntegerField()
    subject5_marks = models.IntegerField()
    subject6_marks = models.IntegerField()

    def __str__(self):
        return self.name
    
    