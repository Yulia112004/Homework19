from catalog.views import index, contacts
from django.urls import path

urlpatterns = [
    path('', index),
    path('contacts/', contacts)
]