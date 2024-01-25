from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.index), 
    path('index/', views.index, name='index'), 
    path('navbar/', views.navbar, name='navbar'), 
    path('footer/', views.footer, name='footer'), 
    path('about/', views.about, name='about'), 
    path('service/', views.service, name='service'), 
    path('service_faculty/', views.service_faculty, name='service_faculty'), 
    path('service_student/', views.service_student, name='service_student'),
    path('event/', views.event, name='event'),  
    path('announcement/', views.announcement, name='announcement'),  
    path('contact/', views.contact, name='contact'),  

]