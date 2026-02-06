from django.contrib import admin
from django.urls import path
from myfinal import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('admin/', admin.site.urls),

    path('',views.homestart, name='homestart'),
    path('signup/',views.signup, name='signup'),
    path('login/',views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    path('teacher_dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('about/',views.about, name='about'),
    path('help/',views.help, name='help'),
    path('teach/about/',views.admin_about, name='admin_about'),
    path('teach/help/',views.admin_help, name='admin_help'),
    path('home/about/',views.home_about, name='home_about'),
    path('home/help/',views.home_help, name='home_help'),

    path('faculty/',views.faculty, name='faculty'),
    path('teach/faculty/',views.admin_faculty, name='admin_faculty'),


    path('add/records/', views.records, name='records'),
    path('delete/records/<str:id>/', views.delete_record, name='delete_record'),
    
    path('add/events/', views.admin_events, name='admin_events'),
    path('events/register/<int:event_id>/', views.register_event, name='register_event'),
    path('show/events/', views.show_events, name='events'), 
    path('delete/events/<int:event_id>/', views.delete_event, name='delete_event'),

    path('add/attendance/', views.add_attendance, name='add_attendance'),
    path('add/attendance/delete/<int:id>/', views.delete_attendance, name='delete_attendance'),
 
    path('show/note/',views.stu_note,name='stu_note'),
    path('add/note/',views.admin_note,name='admin_note'),
    path('delete/<int:id>/',views.delete_note,name='delete_note'),
    
    path('add/notice/',views.admin_notice,name='admin_notice'), 
    path('show/notice/',views.stu_notice,name='stu_notice'),
    path('ndelete/<int:id>/',views.delete_notice,name='delete_notice'),

    path('add/assingment/',views.admin_assingment,name='admin_assingment'),
    path('show/assingment/',views.stu_assingment,name='stu_assingment'),
    path('adelete/<int:id>/',views.delete_assingment,name='delete_assingment'),
   
    path('upload/course/', views.upload_course, name='upload_course'),
    path('show/course/', views.stu_course, name='show_courses'),
    path('deletecourse/<int:id>/',views.delete_course,name='delete_course'),

    

]
# This will serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
