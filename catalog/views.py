from django.shortcuts import render
from catalog.models import Product


def index(request):
    product_list = Product.objects.all()
    context = {
        'objects_list': product_list
    }
    return render(request, 'catalog/index.html', context)

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
    return render(request, 'catalog/contacts.html')


def product(request, pk):
    product_list = Product.objects.filter(id=pk)
    context = {
        'objects_list': product_list
    }
    return render(request, 'catalog/product.html', context)