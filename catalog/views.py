from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from pytils.translit import slugify


from catalog.models import Product, Record


# Create your views here.
def index(request):
    return render(request, 'catalog/index.html')


def contacts(request):
    if request.method == 'POST':
        print(request.POST.get('name'))
        print(request.POST.get('phone'))
        print(request.POST.get('message'))
    return render(request, 'catalog/contacts.html')


# def products(request):
#     context = {
#         'product_list': Product.objects.all()
#     }
#     return render(request, 'catalog/products.html', context)


class ProductListView(ListView):
    model = Product

class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('catalog:product_list')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class ProductDetailView(DetailView):
    model = Product


class RecordListView(ListView):
    model = Record


class RecordCreateView(CreateView):
    model = Record
    fields = ('title', 'content', 'image')
    success_url = reverse_lazy('catalog:record_list')


class RecordUpdateView(UpdateView):
    model = Record
    fields = ('title', 'content', 'image')
    success_url = reverse_lazy('catalog:record_detail')


class RecordDeleteView(DeleteView):
    model = Record
    success_url = reverse_lazy('catalog:record_list')


class RecordDetailView(DetailView):
    model = Record

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views_counter += 1
        obj.save()
        return obj



