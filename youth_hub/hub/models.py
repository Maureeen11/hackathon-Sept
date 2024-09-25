from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Model for the UserProfile to extend the default User
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    skills = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username

# Model for projects submitted by users
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=[
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    ])

    def __str__(self):
        return self.title

# Model for Mentors to guide users
class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    expertise = models.CharField(max_length=255)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
