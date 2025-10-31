
from django.urls import path
from . import views


urlpatterns = [
    path('', views.list_policies, name='home'),
    path('register/', views.register_policy, name='register_policy'),
    path('certificate/', views.add_certificate, name='add_certificate'),
]