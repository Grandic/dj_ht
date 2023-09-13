from django.urls import path
from catalog.views import ProductListView, ProductDetailView, index2
from catalog.apps import CatalogConfig
app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='main'),
    path('contacts/', index2, name='contact'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
]