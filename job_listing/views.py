from django.shortcuts import render
from .models import Job

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'job_list.html', {'jobs': jobs})

def job_detail(request, pk):
    job = Job.objects.get(pk=pk)
    return render(request, 'job_detail.html', {'job': job})
