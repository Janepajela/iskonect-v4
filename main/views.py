from django.shortcuts import render, redirect
from django.http import JsonResponse



# Create your views here.
def index(request):
    return render(request, 'index.html', {'current_page': 'index'})
def navbar(request):
    return render(request, 'navbar.html')
def footer(request):
    return render(request, 'footer.html')
def about(request):
    return render(request, 'about.html', {'current_page': 'about'})
def service(request):
    return render(request, 'service.html')
def service_faculty(request):
    return render(request, 'service_faculty.html')
def service_student(request):
    return render(request, 'service_student.html')
def event(request):
    return render(request, 'event.html')
def announcement(request):
    return render(request, 'announcement.html')
def contact(request):
    return render(request, 'contact.html')