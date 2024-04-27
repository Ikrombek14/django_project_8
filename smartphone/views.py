from django.shortcuts import render
from .models import Brand, Product, Madel

def index_page(request):
    queryset = Brand.objects.all().order_by('name')
    # print(queryset)
    return render(request, 'index.html', {'sort_brand': queryset})

def get_madel(request, madel_id):
    queryset = Madel.objects.all().filter(brand=madel_id)
    print(queryset)
    brand = Brand.objects.get(id=madel_id)
    context = {'filter_madel': queryset, 'brand_name': brand}
    return render(request, 'madel_product.html', context)

def get_product(request, product_id, soni):
    queryset = Product.objects.all().filter(madel=product_id)[:soni]
    print(queryset)
    madel = Madel.objects.get(id=product_id)
    print(madel)
    context = {'madel_pro': queryset, 'madel': madel}
    return render(request, 'phone_product.html', context)