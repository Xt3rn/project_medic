from django.shortcuts import render, redirect
from sert.forms import PolicyForm, CertificateForm
from sert.models import MedicalPolicy, VaccinationCertificate
from django.core.paginator import Paginator

def register_policy(request):
    if request.method == 'POST':
        form = PolicyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PolicyForm()
    return render(request, 'reg_policy.html', {'form': form})

def add_certificate(request):
    if request.method == 'POST':
        form = CertificateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CertificateForm()
    return render(request, 'add_cert.html', {'form': form})

def list_policies(request):
    policies = MedicalPolicy.objects.all().order_by('-id')
    paginator = Paginator(policies, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'list_policies.html', {'page_obj': page_obj})

def previous_page(request):
    current_page = int(request.GET.get('page', 1)) - 1
    if current_page >= 1:
        return redirect(f'/policies/?page={current_page}')
    return redirect('/policies/')

def next_page(request):
    current_page = int(request.GET.get('page', 1))
    next_page_num = current_page + 1
    return redirect(f'/policies/?page={next_page_num}')