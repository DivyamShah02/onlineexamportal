"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from project import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name="home"),
    path('head-admin-sign-up/', views.h_signup,name="head_admin-sign-up"),    
    path('head-admin-sign-in/', views.h_signin,name="head_admin-sign-in"), 
    path('head-admin/dashboard/<id>',views.head_admin_dashboard,name="head_admin_dashboard"),    
    path('head-admin-log-out/<id>', views.ha_log_out,name="ha_logout"),       
    path('student-sign-up/', views.s_signup,name="student-sign-up"),
    path('student-sign-in/', views.s_signin,name="student-sign-in"),
    path('student/change-password', views.s_change_pass,name="student_change_password"),
    path('student-log-out/<s_id>', views.s_log_out,name="s_logout"),
    path('teacher-sign-up/', views.t_signup,name="teacher-sign-up"),
    path('teacher-sign-in/', views.t_signin,name="teacher-sign-in"),
    path('teacher/change-password', views.t_change_pass,name="teacher_change_password"),
    path('teacher-log-out/<t_id>', views.t_log_out,name="t_logout"),
    path('student/dashboard/<id>',views.student_dashboard,name="student_dashboard"),
    path('student/batch/<s_id>/<b_id>',views.batch_student,name="student_batch"),
    path('student/batch/<s_id>/<b_id>/<e_id>',views.test_student,name="student_test"),
    path('teacher/dashboard/<id>',views.teacher_dashboard,name="teacher_dashboard"),
    path('teacher/batch/<t_id>/<b_id>',views.batch_teacher,name="teacher_batch"),
    path('teacher/batch/<t_id>/<b_id>/<e_id>',views.test_teacher,name="teacher_test"),  
    path('delete/',views.delete,name="delete-all"),
    path('feedback/',views.feedback_view,name="feedback"),
    path('student/dashboard/profile/<id>',views.student_profile,name="student_profile"),
    path('teacher/dashboard/profile/<id>',views.teacher_profile,name="teacher_profile"),
    path('head-admin/dashboard/profile/<id>',views.head_admin_profile,name="head_admin_profile"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
