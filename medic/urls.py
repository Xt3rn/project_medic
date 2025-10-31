
from django.urls import path
from . import views


urlpatterns = [
    path('', views.list_policies, name='index'),
    path('register/', views.register_policy, name='register_policy'),
    path('certificate/', views.add_certificate, name='add_certificate'),
    path('previous-page/', views.previous_page, name='previous'),  # Обратите внимание на правильное имя
    path('next-page/', views.next_page, name='next'),
]