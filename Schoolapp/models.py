from django.db import models





# Create your models here.


class tbl_login(models.Model):
    fname = models.CharField(max_length=200,null=True)
    lname = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=100,unique=True,primary_key=True)
    password = models.CharField(max_length=200,null=True)
    department = models.CharField(max_length=100,null=True)
    year_of_join = models.CharField(max_length=100,null=True)
    type = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.email
    


class teacher_detail(models.Model):
    email=models.ForeignKey(tbl_login,on_delete=models.CASCADE, limit_choices_to={'type': 'Teacher'})
    fname = models.CharField(max_length=100, blank=True, null=True)
    lname = models.CharField(max_length=100, blank=True, null=True)
    hname = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(default=0,max_length=200)
    dob = models.DateField(auto_now_add=False)
    caste = models.CharField(max_length=100, blank=True, null=True)
    place = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.email.email


class Student_detail(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=100, blank=True, null=True)
    lname = models.CharField(max_length=100, blank=True, null=True)
    hname = models.CharField(max_length=100, blank=True, null=True)
    father = models.CharField(max_length=100, blank=True, null=True)
    occupation = models.CharField(max_length=100, blank=True, null=True)
    pmobile = models.CharField(blank=True, null=True,max_length=200)
    email = models.ForeignKey(tbl_login,on_delete=models.CASCADE,null=True, limit_choices_to={'email__type': 'Student'})
    profile_pic = models.ImageField(upload_to='student/profile', null=True)
    dob = models.DateField(auto_now_add=False)
    religion = models.CharField(max_length=100, blank=True, null=True)
    pschool = models.CharField(max_length=100, blank=True, null=True)
    mark_obtained = models.CharField(blank=True, null=True,max_length=200)
    gender = models.CharField(max_length=100, blank=True, null=True)
    gname = models.CharField(max_length=100, blank=True, null=True)
    gmobile = models.CharField(blank=True, null=True,max_length=200)
    gemail = models.EmailField(default=0, blank=True, null=True)

    def __str__(self):
        return self.fname
    

class Course(models.Model):
        course_id = models.AutoField(primary_key=True,null=False)
        Course_name = models.CharField(max_length=100,blank=True, null=True)
        Course_img = models.ImageField(upload_to='course/subject', null=True)
        Description = models.CharField(max_length=100, blank=True, null=True)
        
        def __str__(self):
            return self.Course_name
        


class Class_division(models.Model):
    class_id = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=100, blank=True, null=True)
    Course_name = models.ForeignKey(Course, on_delete=models.CASCADE,null=True)
    # class_teacher = models.ForeignKey(tbl_login, on_delete=models.CASCADE, limit_choices_to={'type': 'Teacher'})

    def __str__(self):
        return f"{self.class_name} - {self.Course_name}"




class Class_teachers(models.Model):
    class_id = models.AutoField(primary_key=True)
    class_name = models.ForeignKey(Class_division, on_delete=models.CASCADE,null=True)
    Course_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    class_teacher = models.ForeignKey(tbl_login, on_delete=models.CASCADE, limit_choices_to={'type': 'Teacher'})

    def __str__(self):
        return f"{self.class_name} - {self.class_teacher}"


#model for creating subjects

class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=100, blank=True, null=True)
    Course_name = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subject_name} - {self.Course_name}"



#model for assigning techers

class Teacher_Subject(models.Model):
    Course_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ManyToManyField(tbl_login,limit_choices_to={'type' : 'Teacher'})

    def __str__(self):
        return f"{self.subject} - {self.teacher}"


class tbl_Subjetfeedback(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return f"{self.subject} - {self.feedback}"




class Exam_type(models.Model):
    exam_name =  models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
         return self.exam_name




class Student_Careerprediction(models.Model):
    id = models.AutoField(primary_key=True)
    df = models.CharField(blank=True, null=True, max_length=200)
    ca = models.CharField(blank=True, null=True, max_length=200)
    dcs = models.CharField(blank=True, null=True, max_length=200)
    cs = models.CharField(blank=True, null=True, max_length=200)
    networking = models.CharField(blank=True, null=True, max_length=200)
    sd = models.CharField(blank=True, null=True, max_length=200)
    ps = models.CharField(blank=True, null=True, max_length=200)
    pm = models.CharField(blank=True, null=True, max_length=200)
    cff = models.CharField(blank=True, null=True, max_length=200)
    tc = models.CharField(blank=True, null=True, max_length=200)
    aiml = models.CharField(blank=True, null=True, max_length=200)
    se = models.CharField(blank=True, null=True, max_length=200)
    ba = models.CharField(blank=True, null=True, max_length=200)
    cskills = models.CharField(blank=True, null=True, max_length=200)
    ds = models.CharField(blank=True, null=True, max_length=200)
    td = models.CharField(blank=True, null=True, max_length=200)
    gd = models.CharField(blank=True, null=True, max_length=200)

    def __str__(self):
        return self.id