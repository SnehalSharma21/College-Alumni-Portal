from django.contrib import admin
from collegeapp.models import Event , Student, Attendance,Notice,Notes,Assingment,Course,User,EventRegistration
# Register your models here.
admin.site.register(Event)
admin.site.register(EventRegistration)
admin.site.register(Student)
admin.site.register(Attendance)
admin.site.register(Notice)
admin.site.register(Notes)
admin.site.register(Assingment)
admin.site.register(Course)
admin.site.register(User)