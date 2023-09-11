from django.urls import path
from catalog.views import index, index2, product
from catalog.apps import CatalogConfig
from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='main'),
    path('contacts/', index2, name='contact'),
    path('product/<int:pk>', product, name='product'),
]