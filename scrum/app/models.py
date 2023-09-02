from django.db import models

# Create your models here.
class Project(models.Model):
    project_name = models.TextField()
    project_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation

    
    def __str__(self) -> str:
        return self.project_name

class Ticket(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    ticket_title = models.TextField()
    ticket_description = models.TextField()
    ticket_status = models.CharField(choices=STATUS_CHOICES, max_length=50)
    
    def __str__(self) -> str:
        return self.ticket_title