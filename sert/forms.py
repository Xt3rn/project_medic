from django import forms
from .models import MedicalPolicy, VaccinationCertificate

class PolicyForm(forms.ModelForm):
    class Meta:
        model = MedicalPolicy
        fields = ['number', 'name', 'surname', 'dadname', 'issue_date']

class CertificateForm(forms.ModelForm):
    class Meta:
        model = VaccinationCertificate
        fields = ['policy', 'vaccination_date', 'vaccine_type', 'comments']