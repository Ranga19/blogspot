from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.

class UserLoginView(LoginView):
    template_name = 'authentication/login.html'
    def get_success_url(self):
        return reverse_lazy('home')
    

class UserRegistrationView(FormView):
    form_class = UserCreationForm
    template_name = 'authentication/register.html'
    success_url = reverse_lazy('home')
    def form_valid(self, form) -> HttpResponse:
        user = form.save()
        user.save()
        return super().form_valid(form)