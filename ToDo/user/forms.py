from django import forms
from django.core.exceptions import ValidationError
from user.models import CustomUser
from django.db import models




class CustomUserForm(models.Model):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    surename = models.CharField(max_length=50)
    email = models.TextField()
    phone = models.IntegerField(blank=False)
    is_active = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean_name(self):
        _username = self.cleaned_data["username"]
        if Task.objects.filter(username=_username).exists():
            raise ValidetionError("username already exists")


class UserModelForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = "__all__"