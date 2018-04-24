from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("Hello, world. You're at the index.")

def StudentsPage(request):
	return render(request,'theMainSite/StudentView.html')

def FacultyPage(request):
	return render(request,'theMainSite/FacultyView.html')

def RegistrationPage(request):
	return render(request,'theMainSite/Registration.html')

def SignIn(request):
	return render(request,'theMainSite/SignIn.html')
def MakeCourse(request):
        info = CourseForm(request.POST)
        if info.is_valid():
                cleanData = info.cleaned_data
                newCourse = Courses(course_id=cleanData['courseNumber'] ,courseName=cleanData['courseName'])
        else:
                info = CourseForm()
        return render(request,'theMainSite/FacultyView.html')
