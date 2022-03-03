from django.contrib.auth.models import User
from django.db import models


class CustomUser(models.Model):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    surename = models.CharField(max_length=50)
    email = models.TextField()
    phone = models.IntegerField(blank=False)
    is_active = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username}-{self.created_at}"



