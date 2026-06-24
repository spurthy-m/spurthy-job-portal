from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def jobs(request):
    jobs = [
        {
            "title": "Python Developer",
            "company": "Infosys",
            "location": "Bangalore",
            "description": "Work on Django backend development"
        },
        {
            "title": "Frontend Developer",
            "company": "TCS",
            "location": "Chennai",
            "description": "Work on HTML, CSS and JavaScript UI"
        },
        {
            "title": "Data Analyst",
            "company": "Wipro",
            "location": "Hyderabad",
            "description": "Work on data analysis and reports"
        }
    ]

    return render(request, 'jobs.html', {'jobs': jobs})


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def recruiter_register(request):
    return render(request, 'recruiter_register.html')

def recruiter_login(request):
    return render(request, 'recruiter_login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def profile(request):
    return render(request, 'profile.html')

def resume_upload(request):
    return render(request, 'resume_upload.html')

def job_details(request):
    return render(request, 'job_details.html')

def apply_job(request):
    return render(request, 'apply_job.html') i