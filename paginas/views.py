from django.shortcuts import render


def home(request):
    return render(request, "paginas/home.html")


def portfolio(request):
    return render(request, "paginas/portfolio.html")
