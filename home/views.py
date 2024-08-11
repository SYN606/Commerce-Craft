from django.shortcuts import render


def home(request):
    if request.user.is_authenticated:
        data = {"user": request.user, "title": "Homepage"}
        return render(request, "index.html", data)
    else:
        data = {"title": "Homepage"}
        return render(request, "index.html", data)
