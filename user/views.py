from django.shortcuts import render, redirect
from django.contrib.auth.models import auth  # type: ignore
from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model()


def login(request):
    data = {"title": "Login into your account"}
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "You're now logged in.")
            return redirect("homepage")
        else:
            messages.info(request, "Invalid Credentials")
            return redirect("login")
    else:
        return render(request, "login.html", data)


def create_account(request):
    data = {"title": "Create your new account here."}
    if request.method == "POST":
        first_name = request.POST["f_name"]
        last_name = request.POST["l_name"]
        email = request.POST["email"]
        password = request.POST["passwd"]
        passd2 = request.POST["passwd2"]
        mobile_number = request.POST["mobile_number"]

        if password == passd2:
            name = first_name + last_name
            new_user = User.objects.create_user(
                                name=name, email=email, password=password, phone_number=mobile_number
                                ) # type: ignore
            
            new_user.save()
            messages.info(request, "Your account is created successfully.")
            return redirect("login")
        else:
            messages.info(request, "Password did not match.")
            return redirect("create_acc")
    else:
        return render(request, "create-acc.html", data)
