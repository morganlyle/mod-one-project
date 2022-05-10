from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            messages.success(request, "account Created successfully")
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "registration/login.html", {"form": form})
