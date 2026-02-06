from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

#this models define all records of student in database
class Student(models.Model):
    id = models.CharField( primary_key=True, max_length=10)
    name = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    password=models.CharField(max_length=20)

from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length=100)  # Signup ke 'username' field yaha save hoga
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)   # store hashed password
    role = models.CharField(
        max_length=20,
        choices=[
            ('student', 'Student'),
            ('teacher', 'Teacher'),
            ('admin', 'Admin')
        ],
        default='student'
    )

    def _str_(self):
        return f"{self.full_name} ({self.role})"

def __str__(self):
    return f"{self.username}"
# this models define all attendance records in database

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)   # to create rela.betw.stu.and att.
    subject = models.CharField(max_length=100)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Present','Present'),('Absent','Absent'),('Late','Late'),('Leave','Leave')])
    created_at = models.DateTimeField(auto_now_add=True)

# this models define all events in database
class Event(models.Model):
    EVENT_TYPES = [
        ('Technical', 'Technical'),
        ('Sports', 'Sports'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    category = models.CharField(max_length=20, choices=EVENT_TYPES,blank=False,null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class EventRegistration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    registration_date = models.DateTimeField(default=timezone.now)

    def _str_(self):
        return f"{self.name} - {self.event.title}"
    
class Notice(models.Model):
    nName=models.CharField(max_length=100)
    nDescription=models.TextField()
    nDate=models.DateField()
    nTime=models.TimeField()
    updatedBy=models.CharField(max_length=20)
    notice_type = [
    ('exam', 'Exam'),
    ('event', 'Event'),
    ('holiday', 'Holiday'),
    ('circular', 'Circular'),
    ('placement', 'Placement'),
    ('general', 'General'),
    ]
    category = models.CharField(  max_length=20,choices=notice_type,default='general')

class Notes(models.Model):
    note=models.CharField(max_length=50)
    ndescribe=models.TextField()
    ndate=models.DateField()
    ntime=models.TimeField()
    updatedby=models.CharField(max_length=50)
    file=models.FileField(upload_to='notes/')
    sub=models.CharField(max_length=20)
def __str__(self):
        return self.note
    

class Assingment(models.Model):
    assin=models.CharField(max_length=50)
    adescribe=models.TextField()
    adate=models.DateField()
    atime=models.TimeField()
    aupdatedby=models.CharField(max_length=50)
    afile=models.FileField(upload_to='notes/')
    asub=models.CharField(max_length=20)


 
def __str__(self):
        return self.note

from django.db import models

class Course(models.Model):
    cname = models.CharField(max_length=100)
    cdesc = models.TextField()
    cfile = models.FileField(upload_to='courses/')
    uploaded_by = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)

    def _str_(self):
        return self.cname


