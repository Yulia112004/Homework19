from PIL import Image
from django.shortcuts import render
from django.views import View

from catalog.forms import ProductForm
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from catalog.models import Product, Contact

# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = "main/index.html"
    paginate_by = 1


class ContactListView(ListView):
    model = Contact
    template_name = "main/contacts.html"
    context_object_name = "adress_info"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Контакты'
        return context

    def post(self, request, *args, **kwargs):
        country = request.POST.get('country')
        inn = request.POST.get('inn')
        address = request.POST.get('address')
        print(f'{country}\n{inn}\n{address}')
        contact_obj = Contact(country=country, inn=inn, address=address)
        contact_obj.save()
        return self.get(request, *args, **kwargs)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/product_card.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'О товаре'
        return context


class CreateProductView(View):
    def get(self, request, *args, **kwargs):
        form = ProductForm()
        return render(request, 'main/create_product.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            my_model = form.save(commit=False)
            my_model.save()
            image_file = request.FILES['image']
            image = Image.open(image_file)
        return render(request, 'main/index.html', {'form': form})