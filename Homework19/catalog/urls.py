from catalog import views
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ContactListView, CreateProductView
from django.urls import path



app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', ContactListView.as_view(), name='contacts'),
    path('create_product/', CreateProductView.as_view(), name='create_product'),
]