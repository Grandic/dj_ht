from django.urls import path
from catalog.views import ProductListView, ProductDetailView, index2, ProductCreateView, ProductUpdateView
from catalog.apps import CatalogConfig
app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='main'),
    path('contacts/', index2, name='contact'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
]