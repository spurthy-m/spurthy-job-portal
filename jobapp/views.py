from .models import Job

def home(request):
    jobs = Job.objects.all()
    return render(request, 'home.html', {'jobs': jobs})
