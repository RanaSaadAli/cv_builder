from django.shortcuts import render, redirect
from .models import JobApplication
from .forms import JobApplicationForm

# Create your views here.

def applications_list(request):
    applications = JobApplication.objects.all()
    return render(request, 'job_applications/applications_list.html', {'applications':applications})


def add_application(request):

    if request.method == 'POST':
        #handle form submission
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('applications_list')

    else:
        #form display
        form = JobApplicationForm()

    return render(request, 'job_applications/add_application.html', {'form':form})

def update_status(request, application_id):
    application = JobApplication.objects.get(id=application_id)
    application.status = request.POST.get('status')
    application.save()
    return redirect('applications_list')