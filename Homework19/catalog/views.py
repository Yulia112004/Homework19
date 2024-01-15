from PIL import Image
from django.shortcuts import render
from catalog.forms import ProductForm
from django.core.paginator import Paginator

from catalog.models import Product, Contact

# Create your views here.
def index(request):
    all_products = Product.objects.all()
    paginator = Paginator(all_products, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "main/index.html", {'page_obj': page_obj})

def contacts(request):
    context = {
        'title': 'Контакты',
        'adress_info': Contact.objects.all(),
    }
    if request.method == 'POST':
        country = request.POST.get('country')
        inn = request.POST.get('inn')
        adress = request.POST.get('adress')
        print(f'{country}\n{inn}\n{adress}')
        cost_obj = Contact(country=country, inn=inn, adress=adress)
        cost_obj.save()
    return render(request, "main/contacts.html", context=context)



def product_card(request, pk: int):
    product = Product.objects.get(pk=pk)
    context = {
        'title': 'О товаре',
        "product": product
    }
    return render(request, "main/product_card.html", context=context)


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            my_model = form.save(commit=False)
            my_model.save()
            image_file = request.FILES['image']
            image = Image.open(image_file)
    else:
        form = ProductForm()
    return render(request, 'main/create_product.html', {'form': form})