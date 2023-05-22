
from django.urls import path
from django import forms, views
from django.contrib import admin
from Schoolapp.models import Class_division, Class_teachers, Course, Exam_type, Student_Careerprediction, Student_detail, Teacher_Subject, tbl_login, Subject, teacher_detail
from django.shortcuts import render
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()

class StudentAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'email', 'password', 'department', 'year_of_join', 'type')

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv)]
        return new_urls + urls

    def upload_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]

            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
            
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            for x in csv_data:
                 fields = x.split(",")
                 if len(fields) < 6:
                    messages.warning(request, 'Missing fields in CSV data')
                    return HttpResponseRedirect(request.path_info)
                 if tbl_login.objects.filter(email=fields[2]).exists():
                     continue
                 else:
                 
                   created = tbl_login.objects.update_or_create(
                        fname = fields[0],
                        lname = fields[1],
                        email = fields[2],
                        password = fields[3],
                        department = fields[4],
                        year_of_join = fields[5],
                        type = fields[6],
                        )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)

admin.site.register(tbl_login,StudentAdmin)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Student_detail)
admin.site.register(teacher_detail)
admin.site.register(Teacher_Subject)
admin.site.register(Class_division)
admin.site.register(Class_teachers)
admin.site.register(Student_Careerprediction)
admin.site.register(Exam_type)


# admin.site.register(tbl_Batch)
# admin.site.register(Session)

