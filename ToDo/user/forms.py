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

    # def clean_name(self):
    #     _username = self.cleaned.data["username"]
    #     if CustomUser.objects.filter(username=_username).exists():
    #         raise ValidationError("username already exists")


class UserModelForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = "__all__"

    def clean_username(self):
        _username = self.cleaned_data["username"]
        if CustomUser.objects.filter(username=_username).exists():
            raise ValidationError("username already exists")

    def clean_phone(self):
        _phone = self.cleaned_data["phone"]
        if CustomUser.objects.filter(phone=_phone).exists():
            raise ValidationError("account with this phone numner already exists")

