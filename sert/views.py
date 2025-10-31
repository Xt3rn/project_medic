from django.shortcuts import render, redirect
from .forms import PolicyForm, CertificateForm
from .models import MedicalPolicy, VaccinationCertificate
from django.core.paginator import Paginator

def register_policy(request):
    if request.method == 'POST':
        form = PolicyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PolicyForm()
    return render(request, 'register_policy.html', {'form': form})

def add_certificate(request):
    if request.method == 'POST':
        form = CertificateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CertificateForm()
    return render(request, 'add_certificate.html', {'form': form})

def list_policies(request):
    policies = MedicalPolicy.objects.all().order_by('-id')
    paginator = Paginator(policies, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'list_policies.html', {'page_obj': page_obj})

