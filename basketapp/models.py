from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.db.models import Sum

from mainapp.models import Product


class BasketPosition(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    add_datatime = models.DateTimeField(auto_now_add=True)
