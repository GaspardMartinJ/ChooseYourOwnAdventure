from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    last_choice = models.CharField(max_length=255, blank=True, null=True, default="start")
    clicks = models.PositiveIntegerField(default=0)
    
    def str(self):
        return f"Player {self.username}"