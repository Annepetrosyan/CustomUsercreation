from django.shortcuts import render, HttpResponse
from Task.forms import TaskForm, TaskModelForm
from Task.models import Task


# def home(request):
#     form = TaskForm()
#
#     if request.method == "POST":
#         form = TaskForm(request.POST)
#
#         if form.is_valid():
#             print(form.cleaned_data)
#             # name = form.cleaned_data["name"]
#             # description = form.cleaned_data["description"]
#             # Task.objects.create(name=name, description=description)
#             Task.objects.create(**form.cleaned_data)
#             return HttpResponse("Task is created")
#
#     context = {"form": form}
#
#     return render(request, "task/home.html", context)

def home(request):
    form = TaskModelForm()

    if request.method == "POST":
        form = TaskModelForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponse("Task is created")

    context = {"form": form}

    return render(request, "task/home.html", context)