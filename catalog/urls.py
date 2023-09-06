from django.urls import path
from catalog.views import index, index2
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index),
    path('about', index2)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)