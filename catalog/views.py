from django.shortcuts import render
from catalog.models import Product
from django.views.generic import ListView, DetailView


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
