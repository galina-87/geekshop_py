import json
import os

from django.conf import settings
from django.core.management import BaseCommand

from authapp.models import ShopUser
from mainapp.models import CategoryProduct, Product


def load_from_json(file_name):
    with open(
        os.path.join(settings.JSON_PATH, f'{file_name}.json'),
        encoding='UTF-8'
    ) as infile:
        return json.load(infile)


class Command(BaseCommand):
    help = 'fill in the database from a file',

    def handle(self, *args, **options):
        categories = load_from_json('categories')

        CategoryProduct.objects.all().delete()
        [CategoryProduct.objects.create(**category) for category in categories]

        products = load_from_json('products')
        Product.objects.all().delete()
        for product in products:
            category_name = product['category']
            _category = CategoryProduct.objects.get(name=category_name)
            product['category'] = _category
            new_product = Product(**product)
            new_product.save()

        if not ShopUser.objects.filter(username = 'django').exists():
            ShopUser.objects.create_superuser(username = 'django', email = 'admin@geekshop.ru', password = 'geekbrains')
