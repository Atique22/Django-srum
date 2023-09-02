from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProjectForm, TicketForm
# Create your views here.
def home(request):
    return render(request, 'index.html')

def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index.html')  # Redirect to a success page
    else:
        form = ProjectForm()
    
    return render(request, 'index.html', {'form': form})
