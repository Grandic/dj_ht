from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import ProductListView, ProductDetailView, index2, ProductCreateView, ProductUpdateView
from catalog.apps import CatalogConfig
app_name = CatalogConfig.name

urlpatterns = [
    path('', cache_page(60*60)(ProductListView.as_view()), name='main'),
    path('contacts/', index2, name='contact'),
    path('view/<int:pk>/', cache_page(60*60)(ProductDetailView.as_view()), name='view_product'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
]