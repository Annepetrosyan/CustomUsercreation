from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from user.forms import CustomUserForm,UserModelForm

# Create your views here.
def home(request):
    user_form = UserCreationForm()
    if request.method == "POST":
        print(request.POST)
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()

    context = {"form" : user_form}

    return render(request, "user/home.html", context)

def usercreate(request):
    form_1 = UserModelForm()
    if request.method == "POST":
        print(request.POST)
        form_1 = UserModelForm(request.POST)
        if form_1.is_valid():
            form_1.save()

    context = {"form": form_1}

    return render(request, "user/home.html", context)


