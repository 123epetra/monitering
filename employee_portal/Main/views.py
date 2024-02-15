from django.shortcuts import render ,redirect ,get_object_or_404
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

# def coform(request):
#     form = contact_form()
#     if request.method == 'POST':
#         form = contact_form(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(request.META.get('HTTP_REFERER', 'home'))
#     context = {'form':form}
#     return render(request, 'Main/coform.html', context)

# views.py
def coform(request, company_id=None):
    company_instance = get_object_or_404(company, pk=company_id) if company_id else None
    form = contact_form(initial={'company': company_instance}) if company_instance else contact_form()
    
    if request.method == 'POST':
        form = contact_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.META.get('HTTP_REFERER', 'home'))
    context = {'form': form}
    return render(request, 'Main/coform.html', context)



def contact(request,pk):
    company_instance = get_object_or_404(company, pk=pk)

    # Then, filter contact_info objects by the company
    contacts = contact_info.objects.filter(company=company_instance)

    context = {'contacts':contacts, 'company_id':pk}
    return render (request, 'Main/contact.html', context)
def company_delete(request,pk):
    companies= company.objects.get(id=pk)
    if request.method == 'POST':
        companies.delete()
        return redirect('home')
    
    return render (request, 'Main/delete.html')

def coform_update(request,pk):
    contact = contact_info.objects.get(id = pk)
    form = contact_form(instance=contact)
    if request.method == 'POST':
        form = contact_form(request.POST,instance = contact)
        if form.is_valid():
            saved_contact = form.save()
            # Assuming you want to redirect to the 'contact' view for the company of this contact
            return redirect('contact', pk=saved_contact.company.id)
    return render (request, 'Main/coform.html',{'form':form})


def cpform_update(request,pk):
    companys = company.objects.get(id = pk)
    form = company_form(instance=companys)
    if request.method == 'POST':
        form = company_form(request.POST,instance = companys)
        if form.is_valid():
            form.save()
            # Assuming you want to redirect to the 'contact' view for the company of this contact
            return redirect('home')
    return render (request, 'Main/cpform.html',{'form':form})



