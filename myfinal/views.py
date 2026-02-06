from django.shortcuts import render, redirect, get_object_or_404
from collegeapp.models import Event, Attendance , Student , Notice , Notes , Assingment , Course , User ,EventRegistration
from django.utils import timezone
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password


# PUBLIC: shows cards to students


def sample(request):
    return render (request,'sample.html')


def homestart(request):
    return render (request,'homepage.html')

def teacher_dashboard(request):
    return render (request,'admin_dashboard.html')

def student_dashboard(request):
    return render (request,'student_dash.html')

def about(request):
    return render(request,'about.html')

def help(request):
    return render(request,'help.html')


def admin_about(request):
    return render(request,'admin_about.html')

def admin_help(request):
    return render(request,'admin_help.html')

def home_about(request):
    return render(request,'home_about.html')

def home_help(request):
    return render(request,'home_help.html')

def faculty(request):
    return render(request,'faculty.html')

def admin_faculty(request):
    return render(request,'admin_faculty.html')

def signup(request):
    if request.method == "POST":
        full_name = request.POST.get("username").strip()
        email = request.POST.get("email").strip().lower()
        password = request.POST.get("password")
        role = request.POST.get("role").strip().lower()

        # Basic validation
        if User.objects.filter(email=email).exists():
            return render(request, "login.html", {"error": "Email already exists"})

        if role not in ["student", "teacher"]:
            return render(request, "login.html", {"error": "Invalid role selected"})

        # Save user
        User.objects.create(
            full_name=full_name,
            email=email,
            password=make_password(password),
            role=role
        )
        return render(request, "login.html", {"success": "Account created! Please log in."})

    return render(request, "login.html")

def login(request):
    if request.method == "POST":
        email = request.POST.get("email").strip().lower()
        password = request.POST.get("password")

        user = User.objects.filter(email=email).first()

        if user and check_password(password, user.password):
            # Role-based redirect
            if user.role == "teacher":
                return redirect("admin_events")
            elif user.role == "student":
                return redirect("events")
            else:
                return render(request, "login.html", {"error": "Role not assigned"})

        return render(request, "login.html", {"error": "Invalid email or password"})

    return render(request, "login.html")


def logout(request):
    if 'user_id' in request.session:   # agar session me user id stored hai
        del request.session['user_id'] # session se remove karo
    request.session.flush()  # pura session clear
    messages.success(request, "Logged out successfully!")
    return redirect('login')  # 'login' is your url name

# ADMIN: allows teacher/admin to add + preview events
def admin_events(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        date= request.POST.get('date')
        time = request.POST.get('time')
        category=request.POST.get('category')

        if title and description and date and time and category:
            Event.objects.create(title=title, description=description , date=date, time=time,category=category)
            return redirect('admin_events')  # reload after submit
    events = Event.objects.all().order_by('-created_at')
    return render(request, 'admin_events.html', {'events': events})

def register_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        EventRegistration.objects.create(
            event=event,
            name=name,
            email=email,
            phone=phone
        )

        messages.success(request, f"Successfully registered for {event.title}!")
        return redirect('register_event', event_id=event.id)

    return render(request, 'register.html', {'event': event})

# ADMIN: allows teacher/admin to delete events
def delete_event(request, event_id):
    try:
        event = Event.objects.get(id=event_id)
        event.delete()
    except Event.DoesNotExist:
        pass  # Handle the case where the event does not exist
    return redirect('admin_events')  # Redirect to the admin events page after deletion

def show_events(request):
    tech_events = Event.objects.filter(category='Technical')
    sport_events = Event.objects.filter(category='Sports')
    return render(request, 'event.html', {
        'tech_events': tech_events,
        'sport_events': sport_events
    })
# ADMIN: allows teacher/admin to manage attendance
# Show attendance dashboard
def add_attendance(request):
    # take input from form
    if request.method == 'POST':
        student_id = request.POST.get('student')  # HTML form input name="Student"
        subject = request.POST['subject']     # input name="subject"
        date = request.POST['date']           # input name="date"
        status = request.POST['status']       # input name="status"

        # Get the Student object using the ID
        student_obj = Student.objects.get(id=student_id) # id:Stu.stu_id:form
               # stu_obj=stu_obj.id,name,email
               # bec it's compulsory to pass complete obj to foreignkey not only id
              
        # Create an Attendance record linked to that student
        Attendance.objects.create(student=student_obj, subject=subject, date=date, status=status)
  
        return redirect('add_attendance')  # Reload page after POST
              # now updates are visible
              # when this time funt. calls method is get and know in form slect_stu. part new student is visible to do net entry and this cycle continuoes 
    # For GET request — show  form
    attendance_records = Attendance.objects.select_related('student').order_by('-date')
    students = Student.objects.all()       # to show all stu. in -select stu.- dropdown list

    # to display records in table
    return render(request, 'admin_attendance.html', {
        'records': attendance_records,
        'students': students,
        'today': timezone.now().date()
    })

# Delete record
def delete_attendance(request, id):
    Attendance.objects.get(id=id).delete()
    return redirect('add_attendance')

# ADMIN: allows teacher/admin to manage student records
def records(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        email = request.POST.get('email')

        if id and name and email:
            Student.objects.create(id=id, name=name, email=email)
            return redirect('records')  # reload after submit

    students = Student.objects.all()
    return render(request, 'records.html', {'students': students})

def delete_record(request, id):
    # Safely get the student or return 404 if not found
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('records')

def admin_notice(request):
    
    if request.method == 'POST':
      nName = request.POST.get('nName')
      nDescription = request.POST.get('nDescription')
      nDate = request.POST.get('nDate')
      nTime = request.POST.get('nTime')
      updatedBy = request.POST.get('updatedBy')
      category=request.POST.get('category')
      if nName and nDescription and nDate and nTime and updatedBy and category:
        Notice.objects.create(nName=nName,nDescription=nDescription,nDate=nDate,nTime=nTime,updatedBy=updatedBy,category=category)
        return redirect('admin_notice')
    
    notices=Notice.objects.all()
    return render(request,'admin_notice.html',{'notices':notices})

def stu_notice(request):
   
      event = Notice.objects.filter(category='event')
      holiday = Notice.objects.filter(category='holiday')
      circular= Notice.objects.filter(category='circular')
      placement = Notice.objects.filter(category='placement')
      general = Notice.objects.filter(category='general')
      exam = Notice.objects.filter(category='exam')
      return render(request, 'stu_noticeboard.html', {
              'exams':exam,
              'events':event,
              'holidays':holiday,
              'circulars':circular,
              'placements':placement,
              'general':general,
             })

def delete_notice(request, id):
    notice = get_object_or_404(Notice, id=id)

    if request.method == 'POST':
        notice.delete()

    return redirect('admin_notice')

# ✅ Admin Panel View – Upload & Display Notes
def admin_note(request):
    if request.method == 'POST':
        note = request.POST.get('note')
        ndescribe = request.POST.get('ndescribe')
        ndate = request.POST.get('ndate')
        ntime = request.POST.get('ntime')
        updatedby = request.POST.get('updatedby')
        file = request.FILES.get('file')  # file from form
        sub = request.POST.get('sub')

        if note and ndescribe and ndate and ntime and updatedby and file and sub:
            Notes.objects.create(
                note=note,
                ndescribe=ndescribe,
                ndate=ndate,
                ntime=ntime,
                updatedby=updatedby,
                file=file,
                sub=sub
            )
            return redirect('admin_note')

    query = request.GET.get('q')
    notes = Notes.objects.all().order_by('-ndate', '-ntime')

    if query:
        notes = notes.filter(
            Q(note__icontains=query) |
            Q(sub__icontains=query)
        )

    return render(request, 'admin_notes.html', {'notes': notes, 'query': query})


# ✅ Delete Note (Admin Only)
def delete_note(request, id):
    note = get_object_or_404(Notes, id=id)

    if request.method == 'POST':
        if note.file:
            note.file.delete()  # Optional: delete actual uploaded file
        note.delete()

    return redirect('admin_note')


# ✅ Student Notes Panel – View & Search Only
def stu_note(request):
    query = request.GET.get('q')
    notes = Notes.objects.all().order_by('-ndate', '-ntime')

    if query:
        notes = notes.filter(
            Q(note__icontains=query) | # here | is using for or operation
            Q(sub__icontains=query)
        )

    return render(request, 'stud_notes.html', {
        'notes': notes,
        'query': query
    })


# ✅ Admin panel to upload & view assignments
def admin_assingment(request):
    if request.method == 'POST':
        assin = request.POST.get('assin')
        adescribe = request.POST.get('adescribe')
        adate = request.POST.get('adate')
        atime = request.POST.get('atime')
        aupdatedby = request.POST.get('aupdatedby')
        asub = request.POST.get('asub')
        afile = request.FILES.get('afile')

        if assin and adescribe and adate and atime and aupdatedby and asub and afile:
            Assingment.objects.create(
                assin=assin,
                adescribe=adescribe,
                adate=adate,
                atime=atime,
                aupdatedby=aupdatedby,
                asub=asub,
                afile=afile
            )
            return redirect('admin_assingment')

    query = request.GET.get('q')
    assingments = Assingment.objects.all().order_by('-adate', '-atime')

    if query:
        assingments = assingments.filter(
            Q(assin__icontains=query) |
            Q(asub__icontains=query)
        )

    return render(request, 'admin_assingment.html', {
        'assingments': assingments,
        'query': query
    })


# ✅ Student panel to view & download assignments
def stu_assingment(request):
    query = request.GET.get('q')
    assingments = Assingment.objects.all().order_by('-adate', '-atime')

    if query:
        assingments = assingments.filter(
            Q(assin__icontains=query) |
            Q(asub__icontains=query)
        )

    return render(request, 'stu_assingment.html', {
        'assingments': assingments,
        'query': query
    })


# ✅ Delete assignment (admin only)
def delete_assingment(request, id):
    assingment = get_object_or_404(Assingment, id=id)
    if request.method == 'POST':
        if assingment.afile:
            assingment.afile.delete()  # delete file from media folder
        assingment.delete()
    return redirect('admin_assingment')


def upload_course(request):
    if request.method == 'POST':
        cname = request.POST['cname']
        cdesc = request.POST['cdesc']
        cfile = request.FILES['cfile']
        uploaded_by = request.POST['uploaded_by']
        Course.objects.create(cname=cname, cdesc=cdesc, cfile=cfile, uploaded_by=uploaded_by)
        return redirect('upload_course')
    courses = Course.objects.all().order_by('-id')  # latest first
    return render(request, 'admin_course.html',{'courses':courses})


def stu_course(request):
    
    query = request.GET.get('q')
    courses = Course.objects.all().order_by('-date')

    if query:
        courses = courses.filter(
            Q(cname__icontains=query) |
            Q(cdesc__icontains=query)
        )

    return render(request, 'stu_course.html', {
        'courses': courses,
        'query': query
    })


def delete_course(request, id):
    course = get_object_or_404(Course, id=id)
    if request.method == 'POST':
        if course.cfile:
            course.cfile.delete()  # delete file from media folder
        course.delete()
    return redirect('upload_course')
