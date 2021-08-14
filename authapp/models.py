from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class ShopUser(AbstractUser):
    userphoto = models.ImageField(name='photo', upload_to='user_photo', default='user_photo/logo.png')
    ageuser = models.SmallIntegerField(verbose_name='возраст', name='age', blank=True, default=0)

    def col_prod(self):
        return sum(position.quantity for position in self.basketposition_set.all())

    def cost_prod(self):
        return sum(position.product.price * position.quantity for position in self.basketposition_set.all())
