from django.shortcuts import render


def home(request):
    data = {"title": "Homepage"}
    return render(request, "index.html", data)

