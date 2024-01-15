from catalog import views
from catalog.apps import CatalogConfig
from catalog.views import index, contacts, create_product
from django.urls import path



app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('create_product/', create_product, name='create_product'),
]