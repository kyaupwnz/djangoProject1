from django.shortcuts import render

from catalog.models import Product


# Create your views here.
def index(request):
    return render(request, 'catalog/index.html')


def contacts(request):
    if request.method == 'POST':
        print(request.POST.get('name'))
        print(request.POST.get('phone'))
        print(request.POST.get('message'))
    return render(request, 'catalog/contacts.html')


def products(request):
    context = {
        'product_list': Product.objects.all()
    }
    return render(request, 'catalog/products.html', context)
