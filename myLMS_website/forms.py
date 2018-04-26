from django import forms
from myLMS_website.models import User, Students
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField()
    first_name = forms.CharField()
    student_id = forms.IntegerField()
    email = forms.EmailField(required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'student_id',
            'email',
            'password1',
            'password2'
        )
    @transaction.atomic
    def save(self):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.is_student = True
        user.save()

        student = Students.objects.create(user=user)
        student.student_id = self.cleaned_data['student_id']
        student.save()

        return user
