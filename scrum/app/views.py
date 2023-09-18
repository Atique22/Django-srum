from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import ProjectForm, TicketForm
from .models import Project, Ticket
# Create your views here.
def home(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects':projects})
def ticket(request, project_name):
    project = get_object_or_404(Project, project_name=project_name)
    tickets = Ticket.objects.all()
    return render(request, 'tickets.html', {'project':project,'tickets':tickets})

def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to a success page
    else:
        form = ProjectForm()
    
    return render(request, 'index.html', {'form': form})

def delete_project(request, project_name):
    project = get_object_or_404(Project, project_name=project_name)
    if project:
         project.delete()
    return redirect('/')

def create_ticket(request):
    if request.method == 'POST':
        
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save()
            project = get_object_or_404(Project, project_name=ticket.project)
            tickets = Ticket.objects.all()
            return render(request, 'tickets.html', {'project':project,'tickets':tickets})
    else:
        form = TicketForm()
    
    return render(request, 'index.html', {'form': form})

def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if ticket:
         ticket.delete()
    project = get_object_or_404(Project, project_name=ticket.project)
    tickets = Ticket.objects.all()
    return render(request, 'tickets.html', {'project':project,'tickets':tickets})