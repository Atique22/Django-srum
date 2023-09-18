from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import ProjectForm, TicketForm, CreateUserForm
from .models import Project, Ticket



def registrationPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method =='POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                print("register successfully!")
                messages.success(request, "Account was created successfully!")
                return redirect('login')
        content = {'form': form}
        return render(request, 'account/register.html', content)

def loginPage(request):
    
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user = authenticate(request, username=username ,password=password)
        if user is not None:
            print("user login call")
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect!')
            return render(request, 'account/login.html')
    return render(request, 'account/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects':projects})

@login_required(login_url='login')
def ticket(request, project_name):
    project = get_object_or_404(Project, project_name=project_name)
    tickets = Ticket.objects.all()
    return render(request, 'tickets.html', {'project':project,'tickets':tickets})

@login_required(login_url='login')
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to a success page
    else:
        form = ProjectForm()
    
    return render(request, 'index.html', {'form': form})

@login_required(login_url='login')
def delete_project(request, project_name):
    project = get_object_or_404(Project, project_name=project_name)
    if project:
         project.delete()
    return redirect('/')

@login_required(login_url='login')
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

@login_required(login_url='login')
def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if ticket:
         ticket.delete()
    project = get_object_or_404(Project, project_name=ticket.project)
    tickets = Ticket.objects.all()
    return render(request, 'tickets.html', {'project':project,'tickets':tickets})