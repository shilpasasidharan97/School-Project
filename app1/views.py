from django.shortcuts import redirect, render

from adminapp.models import TeacherBasic

# Create your views here.

def homepage(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def login(request):
    msg=""
    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['psw']

        
        staff_exist=TeacherBasic.objects.filter(email_id=username,dob=password).exists()
        if staff_exist:
            staff_data=TeacherBasic.objects.get(email_id=username,dob=password)
            request.session['teacher']=staff_data.t_id
            return redirect('staff:staffhome')
        else:
            msg="username or password is error"
            return render(request,'erp-login.html',{'msg':msg,})

    return render(request,'erp-login.html')