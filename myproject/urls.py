"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from spurthyjobsapp import views

urlpatterns = [
    # Django Admin Panel
    path('admin/', admin.site.urls),

    # Home
    path('', views.home, name='home'),

    # Main Pages
    path('jobs/', views.jobs, name='jobs'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    # Authentication Pages
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),

    # Recruiter Pages
    path('recruiter_register/', views.recruiter_register, name='recruiter_register'),
    path('recruiter_login/', views.recruiter_login, name='recruiter_login'),

    # User Pages
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('resume_upload/', views.resume_upload, name='resume_upload'),

    # Job Actions
    path('job_details/', views.job_details, name='job_details'),
    path('apply_job/', views.apply_job, name='apply_job'),
]