from django.urls import path
from . import views

urlpatterns = [
	path('',views.index,name='index'),
	path('StudentView/',views.StudentsPage,name ='StudentsPage'),
	path('FacultyView/',views.FacultyPage,name='FacultyPage'),
	path('Registration/',views.RegistrationPage,name='Registration'),
	path('SignIn/',views.SignIn,name='Sign In'),
]
