from django.shortcuts import render, redirect
from .models import Company  # Ensure you're using the correct model

# Create your views here.

def index(request):
    return render(request, 'index.html')


def data(request):
    if request.method == 'POST':
        # Get data from the form submission
        name = request.POST.get('name')
        address = request.POST.get('address')
        c_name = request.POST.get('c_name')
        gender = request.POST.get('gender')
        director = request.POST.get('director')
        date = request.POST.get('date')
        company = Company(name=name, address=address, c_name=c_name, gender=gender, director=director, date=date)
        company.save()
        # 

        
    return render(request, 'submit.html')

def submit_details(request):
    submit_details = Company.objects.latest('id')
    return render(request, 'submit_details.html', {'entry': submit_details})

              

def view(request):
    companies = Company.objects.all()  # Fetch all company details from the database
    return render(request, 'db.html', {'companies': companies})


def form(request):
    save = Company.objects.all()  # Fetch all company details from the database
    return render(request, 'form.html', {'data': data})
    

def delete(request):
    a=Company.objects.all()
    a.delete()
    return render(request,'delete.html')

