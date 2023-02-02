from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Record, Version


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
    # fields = '__all__'
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    # fields = '__all__'
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateWithVersionView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:detail')
    template_name = 'catalog/product_form.html'

    def get_success_url(self):
        return reverse('catalog:detail', args=[self.object.pk])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormSet = inlineformset_factory(self.model, Version, form=VersionForm, extra=1)

        if self.request.method == 'POST':
            formset = VersionFormSet(self.request.POST, instance=self.object)
        else:
            formset = VersionFormSet(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        with transaction.atomic():
            self.object = form.save()
            if formset.is_valid():
                formset.instance = self.object
                formset.save()
        return super().form_valid(form)


class ProductDetailView(DetailView):
    model = Product


class RecordListView(ListView):
    model = Record

    def get_queryset(self):
        return Record.objects.filter(is_public=True)


class RecordCreateView(CreateView):
    model = Record
    fields = ('title', 'content', 'image')
    success_url = reverse_lazy('catalog:record_list')


class RecordUpdateView(UpdateView):
    model = Record
    fields = ('title', 'content', 'image')
    success_url = reverse_lazy('catalog:record_detail')

    def get_success_url(self):
        current_slug = self.kwargs['slug']
        return reverse_lazy('catalog:record_detail', kwargs={'slug': current_slug})


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




