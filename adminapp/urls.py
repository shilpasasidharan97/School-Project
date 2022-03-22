from django.urls import path,include
from . import views

app_name='adminapp'

urlpatterns = [
    path('home',views.home,name='home'),
    path('addteacher',views.add_teacher,name='addteacher')
]