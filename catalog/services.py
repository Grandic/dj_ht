from django.conf import settings
from django.core.cache import cache
from catalog.models import Category


def get_cached_categories_for_product(product_pk):
    if settings.CACHE_ENABLED:
        key = f'subject_list_{product_pk}'
        category_list = cache.get(key)
        if category_list is None:
            category_list = Category.objects.filter(category__pk=product_pk)
            cache.set(key, category_list)
    else:
        category_list = Category.objects.filter(category__pk=product_pk)

    return category_list
