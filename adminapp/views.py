from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')


def add_teacher(request):
    return render(request, 'add_teacher.html')


def manage_teacher(request):
    return render(request, 'manage_teacher.html')


def add_student(request):
    return render(request, 'add_student.html')


def manage_student(request):
    return render(request, 'manage_student.html')


def add_parents(request):
    return render(request, 'add_parents.html')


def manage_parents(request):
    return render(request, 'manage_parents.html')


def add_class(request):
    return render(request, 'add_class.html')


def class_list(request):
    return render(request, 'class_list.html')
