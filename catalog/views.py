from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from users.models import User


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index.html'



class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        version = Version.objects.filter(product=context_data['object'], is_active=True).last()
        context_data['version'] = version

        return context_data

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

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:main')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormSet = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
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
            if form.is_valid():
                self.object = form.save()
                if formset.is_valid():
                    formset.instance = self.object
                    formset.save()

        return super().form_valid(form)

