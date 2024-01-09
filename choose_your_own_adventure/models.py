from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    last_choice = models.CharField(max_length=255, blank=True, null=True)
    
    def str(self):
        return f"Player {self.username}"