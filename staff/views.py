from django.shortcuts import render

# Create your views here.

def teacher_home(request):
    return render(request,'staffhome.html')

def profile(request):
    return render(request,'profile.html')