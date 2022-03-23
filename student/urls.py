from django.urls import path
from . import views

app_name='student'

urlpatterns = [
    path('studenthome',views.student_home,name='studenthome'),
]                   