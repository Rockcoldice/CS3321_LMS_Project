# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_student = models.BooleanField(default=True)
    is_teacher = models.BooleanField(default=False)

class Students(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    student_id = models.IntegerField(null=True)
    gpa = models.DecimalField(decimal_places=2, max_digits=3, null=True)

    #def __str__(self):
    #    return "%s %s" % (self.firstName, self.lastName)

    class Meta:
        verbose_name_plural = "Students"

class Faculty(models.Model):
    faculty_id = models.IntegerField(primary_key = True)
    firstName = models.CharField(max_length=40)
    lastName = models.CharField(max_length=40)
    email = models.EmailField()
    password = models.CharField(max_length=64)
    jobTitle = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = "Faculty"

    def __str__(self):
        return "%s %s" % (self.firstName,self.lastName)

class Courses(models.Model):
    course_id = models.IntegerField(primary_key = True)
    courseName = models.CharField(max_length=40)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE,)

    class Meta:
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.courseName

class Grades(models.Model):
    grade_id = models.IntegerField(primary_key = True)
    student = models.ForeignKey(Students,on_delete=models.CASCADE)
    course = models.ForeignKey(Courses,on_delete=models.CASCADE)
    courseGrade = models.IntegerField()

    class Meta:
        verbose_name_plural = "Grades"
