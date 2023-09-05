from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home page"),
    path('create_project', views.create_project, name='create_project'),
    path('tickets/<str:project_name>/', views.ticket, name='tickets page'),
    path('create_ticket', views.create_ticket, name='create_ticket'),
    path('delete_project/<str:project_name>/', views.delete_project, name='delete_project'),

]
