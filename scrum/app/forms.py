# forms.py
from django import forms
from .models import Project, Ticket

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'
