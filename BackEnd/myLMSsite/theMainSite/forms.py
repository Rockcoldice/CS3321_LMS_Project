from django import forms

class CourseForm(forms.Form):
    courseName = forms.CharField()
    courseNumber = forms.IntegerField()
    numberOfStudents = forms.IntegerField()
