from django.urls import path
from catalog.views import home, contacts, product, products
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', home),
    path('contacts/', contacts, name='contacts'),
    path('products/', products, name='products'),
    path('<int:pk>', product, name='product'),
]