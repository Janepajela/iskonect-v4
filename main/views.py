from django.shortcuts import render, redirect
from django.http import JsonResponse



# Create your views here.
def index(request):
    return render(request, 'pages/iskonect_index.html', {'current_page': 'index'})
# def navbar(request):
#     return render(request, 'pages/iskonect_about.html')
# def footer(request):
#     return render(request, 'pages/iskonect_footer.html')
def about(request):
    return render(request, 'pages/iskonect_about.html', {'current_page': 'about'})
def service(request):
    return render(request, 'pages/iskonect_service.html')
def service_faculty(request):
    return render(request, 'pages/iskonect_serv_f.html')
def service_student(request):
    return render(request, 'pages/iskonect_serv_s.html')
def event(request):
    return render(request, 'pages/iskonect_event.html')
def announcement(request):
    return render(request, 'pages/iskonect_announce.html')
def contact(request):
    return render(request, 'pages/iskonect_contact.html')