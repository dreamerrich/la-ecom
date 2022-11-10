from django.shortcuts import render
from .models import product, cart

# Create your views here.
def home(request):
    p = product.objects.all()
    return render(request, 'index.html', {'p':p})

def about(request):
    return render(request, 'about.html')

def product_items(request):
    p = product.objects.all()
    return render(request, 'product.html', {'p':p})

def blog(request):
    return render(request, 'blog_list.html')

def contacts(request):
    return render(request, 'contact.html')

def test(request):
    return render(request, 'testimonial.html')

def main(request):
    return render(request, 'main.html')