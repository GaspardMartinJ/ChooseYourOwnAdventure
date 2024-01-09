from django.db import models
from django.contrib.auth.models import AbstractUser


class Player(models.Model):
    current_page = 0
    # Add any other fields you may need for your player, e.g., name, score, etc.

    def __str__(self):
        return f"Player {self.id}"