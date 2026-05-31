from django.shortcuts import render


def index(request):
    return render(request, "web/index.html")


def verlag(request):
    return render(request, "web/page.html", {"title": "Verlag"})


def shops(request):
    return render(request, "web/page.html", {"title": "Shops"})
