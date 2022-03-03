from django import forms
from Task.models import Task
from django.core.exceptions import ValidationError
from user.models import CustomUser


class TaskForm(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(max_length=1250)

    def clean_name(self):
        _name = self.cleaned_data["name"]
        if Task.objects.filter(name=_name).exists():
            raise ValidetionError("Task already exists")

        return _name

class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"

