from django.shortcuts import render ,redirect
from .models import *
from .forms import *

# Create your views here.
def home (request):
    companies = company.objects.all()
    context = {'company':companies}
    return render(request, 'Main/home.html', context )

def cpform(request):
    form = company_form()
    if request.method == 'POST':
        form = company_form(request.POST)
        if form.is_valid():
            form.save()

            return redirect('home')
              

    context = {'form':form}
    return render(request, 'Main/cpform.html', context)

def coform(request):
    form = contact_form()
    if request.method == 'POST':
        form = contact_form(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'Main/coform.html', context)


def contact(request):
    contacts= contact_info.objects.all()
    context = {'contacts':contacts}
    return render (request, 'Main/contact.html', context)


    

