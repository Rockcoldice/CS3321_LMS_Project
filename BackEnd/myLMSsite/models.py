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
    faculty = models.ForeignKey(Faculty)
    
    def __str__(self):
        return self.courseName

class Enrollments(models.Model):
    enrollment_id = models.IntegerField(primary_key = True)
    student = models.ForeignKey(Students)
    course = models.ForeignKey(Courses)

class Grades(models.Model):
    grade_id = models.IntegerField(primary_key = True)
    student = models.ForeignKey(Students)
    course = models.ForeignKey(Courses)
    courseGrade = models.IntegerField()
