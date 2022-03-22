from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def add_teacher(request):
    return render(request,'add_teacher.html')