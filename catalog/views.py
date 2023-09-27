from django.shortcuts import render
from django.urls import reverse_lazy

from catalog.forms import ProductForm
from catalog.models import Product, Version
from django.views.generic import ListView, DetailView, CreateView, UpdateView


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'


def index2(request):
    return render(request, 'catalog/index2.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST('name')
        phone = request.POST('phone')
        message = request.POST('message')
        print(f'Клиент: {name}\n'
              f'Телефон: {phone}\n'
              f'Сообщение: {message}')

        context = {
            'title': 'Контакты'
        }
        return render(request, 'catalog/contacts.html', context)


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:main')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:main')