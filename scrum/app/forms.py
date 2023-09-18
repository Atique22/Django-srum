# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Project, Ticket

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']