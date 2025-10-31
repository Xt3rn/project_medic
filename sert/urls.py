from django.urls import path
from . import views

app_name = 'sert'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.diplom_detail, name='detail'),
    path('<int:pk>/edit/', views.diplom_edit, name='edit'),
    path('create/', views.diplom_create, name='create'),
]
