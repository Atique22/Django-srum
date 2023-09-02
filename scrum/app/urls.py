from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home page"),
    path('create_project', views.create_project, name='create_project'),
    path('delete_project/<str:project_name>/', views.delete_project, name='delete_project'),

]
