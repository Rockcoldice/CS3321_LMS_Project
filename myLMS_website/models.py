# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Students(models.Model):
    student_id = models.IntegerField(primary_key =True)
    firstName = models.CharField(max_length=40)
    lastName = models.CharField(max_length=40)
    email = models.EmailField()
    password = models.CharField(max_length=25)
    gpa = models.IntegerField()

    def __str__(self):
        return "%s %s" % (self.firstName, self.lastName)

class Faculty(models.Model):
    faculty_id = models.IntegerField(primary_key = True)
    firstName = models.CharField(max_length=40)
    lastName = models.CharField(max_length=40)
    email = models.EmailField()
    password = models.CharField(max_length=40)
    jobTitle = models.CharField(max_length=40)

    def __str__(self):
        return "%s %s" % (self.firstName,self.lastName)

class Courses(models.Model):
    course_id = models.IntegerField(primary_key = True)
    courseName = models.CharField(max_length=40)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE,)

    def __str__(self):
        return self.courseName

class Grades(models.Model):
    grade_id = models.IntegerField(primary_key = True)
    student = models.ForeignKey(Students,on_delete=models.CASCADE)
    course = models.ForeignKey(Courses,on_delete=models.CASCADE)
    courseGrade = models.IntegerField()
