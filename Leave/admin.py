import csv
from django.contrib import admin
from django.http import HttpResponse

from Leave.models import leaveModel, tbl_teacherleave

def export_users(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Users.csv"'
    writer = csv.writer(response)
    writer.writerow(['Name','Email','Leave Date','Leave Reason','Leave Session'])
    leaveModel = queryset.values_list('name', 'email','leaveDate','leaveReason','leaveDiv')
    for user in leaveModel:
        writer.writerow(user)
    return response
export_users.short_description = 'Download Leave Details'

class UserAdmin(admin.ModelAdmin):
    list_display=['name','email','leaveDate','leaveReason','leaveDiv']
    actions = [export_users]
admin.site.register(leaveModel)
admin.site.register(tbl_teacherleave)