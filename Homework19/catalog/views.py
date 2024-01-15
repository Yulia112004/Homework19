from django.shortcuts import render
from catalog.models import Product, Contact

# Create your views here.
def index(request):
    context = {
        'products': Product.objects.all()[:6],
    }
    print(context)
    return render(request, "main/index.html", context=context)

def contacts(request):
    context = {
        'title': 'Contacts',
        'adress_info': Contact.objects.first(),
    }
    if request.method == 'POST':
        visiter = dict()
        visiter['name'] = request.POST.get('name', None)
        visiter['phone'] = request.POST.get('phone', None)
        visiter['message'] = request.POST.get('message', None)
        print(visiter)

    return render(request, "main/contacts.html", context=context)
