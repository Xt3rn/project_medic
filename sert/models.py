from django.db import models


class MedicalPolicy(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    dadname = models.CharField(max_length=100)
    issue_date = models.DateField()
    number = models.CharField(max_length=20)
    

class VaccinationCertificate(models.Model):
    policy = models.ForeignKey(MedicalPolicy, on_delete=models.CASCADE)
    vaccination_date = models.DateField()
    vaccine_type = models.CharField(max_length=100)
    comments = models.TextField(blank=True)
