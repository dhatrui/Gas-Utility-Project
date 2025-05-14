from django.db import models
from django.contrib.auth.models import User

class RequestType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.ForeignKey(RequestType, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    submitted_at = models.DateTimeField(auto_now_add=True)  # Set once on creation
    resolved_at = models.DateTimeField(null=True, blank=True)  # Optional

    def __str__(self):
        return f"{self.user.username} - {self.request_type.name}"

    def is_resolved(self):
        return self.status == 'resolved' and self.resolved_at is not None

    def formatted_submitted_at(self):
        return self.submitted_at.strftime('%d %b %Y, %I:%M %p')

    def formatted_resolved_at(self):
        return self.resolved_at.strftime('%d %b %Y, %I:%M %p') if self.resolved_at else "Not resolved yet"
