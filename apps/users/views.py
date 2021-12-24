from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterUserForm
from .models import NewUser

class RegisterUser(CreateView):
    model = NewUser
    form_class = RegisterUserForm
    template_name = 'usuario/registro.html'
    success_url = reverse_lazy('inicio')

    
