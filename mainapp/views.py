import random

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Sum
from django.shortcuts import render, get_object_or_404
import json

# Create your views here.
from basketapp.models import BasketPosition
from mainapp.models import CategoryProduct, Product

with open('mainapp/jsonapp/links_main_menu.json', encoding="UTF-8") as links_main_menu_json:
    links_main_menu = json.load(links_main_menu_json)

products = Product.objects.all()


def get_menu():
    return CategoryProduct.objects.all()


def get_hot_product():
    products_hot = Product.objects.all()
    return random.choice(products_hot)


def related_prods(product):
    return Product.objects.filter(category=product.category).exclude(id=product.id)[:3]


def index(request):
    context = {
        'title_page': 'главная',
        'links_main_menu': links_main_menu,
        'categories': get_menu(),
    }
    return render(request, 'mainapp/index.html', context)


def catalog(request):
    hot_product = get_hot_product()
    related_products = related_prods(hot_product)

    context = {
        'title_page': 'каталог',
        'links_main_menu': links_main_menu,
        'categories': get_menu(),
        'products': products,
        'hot_product': hot_product,
        'related_products': related_products,
    }
    return render(request, 'mainapp/catalog.html', context)


def page_product(request, pk):
    related_products = related_prods(get_object_or_404(Product, pk=pk))
    context = {
        'title_page': 'каталог',
        'links_main_menu': links_main_menu,
        'categories': get_menu(),
        'products': products,
        'product': get_object_or_404(Product, pk=pk),
        'related_products': related_products,
    }
    return render(request, 'mainapp/page_product.html', context)


def contact(request):
    locations = [
        {
            'city': 'Москва',
            'position': 'ул. Удальцова, д. 18',
            'phone': '8 (495) 565 56 78',
        },
        {
            'city': 'Москва',
            'position': 'ул. Арбат, д. 24/С2',
            'phone': '8 (495) 577 66 23',
        },
        {
            'city': 'В.Новгород',
            'position': 'ул. Московская, д. 23',
            'phone': '8 (8212) 56 56 21',
        },
        {
            'city': 'Санкт-Петербург',
            'position': 'ул. Оптиков, д. 13',
            'phone': '8 (812) 556 00 99',
        },
    ]
    context = {
        'title_page': 'контакты',
        'locations': locations,
        'links_main_menu': links_main_menu,
    }
    return render(request, 'mainapp/contact.html', context)


def prodcat(request, pk, page=1):
    if int(pk) == 0:
        category = {'pk': 0, 'name': 'все'}
        prods = Product.objects.all()
    else:
        category = get_object_or_404(CategoryProduct, pk=pk)
        prods = Product.objects.filter(category=category)

    product_paginator = Paginator(prods, 2)
    try:
        prods = product_paginator.page(page)
    except PageNotAnInteger:
        prods = product_paginator.page(1)
    except EmptyPage:
        prods = product_paginator.page(product_paginator.num_pages)

    context = {
        'title_page': 'каталог',
        'links_main_menu': links_main_menu,
        'categories': get_menu(),
        'category': category,
        'prods': prods,
    }
    return render(request, 'mainapp/prodcat.html', context)
