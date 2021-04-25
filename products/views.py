from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products })
    #return HttpResponse('Hello MAX')


def new(request):
    return HttpResponse('New Products')

#
def about(request):

    return render(request, 'about.html')
#
#
# def cart(request):
#     products = Product.objects.all()
#     return render(request, 'index.html', {'products': products })
#
