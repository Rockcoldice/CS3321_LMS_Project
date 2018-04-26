# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from myLMS_website.forms import RegistrationForm
from django.shortcuts import redirect

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from myLMS_website.models import User
from myLMS_website.forms import RegistrationForm
from django.contrib.auth import login

# Create your views here.
def index(request):
    return render(request, 'index.html')

def courses(request):
    return render(request, 'courses.html')

def about(reguest):
    return render(request, 'about.html')

def logout_view(request):
    logout(request)
    return redirect('/')

class StudentSignUpView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super(StudentSignUpView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')
