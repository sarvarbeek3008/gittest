from django.http import HttpResponse
from django.shortcuts import render

from main.models import Category, Product


def index(request):
    category = Category.objects.all()
    product = Product.objects.all()
    cxt = {
        "categoriy": category,
        "product": product
    }

    return render(request, "main/layout.html", cxt)


def about(request):
    return HttpResponse("<h1>About bo'limi </h1>")
