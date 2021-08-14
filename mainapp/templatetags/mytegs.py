from django import template
from django.conf import settings

register = template.Library()


@register.filter(name='sale5')
def sale5(price):
    """
    Автоматически делает скидку 5% - относительно вывода поля
    """

    return float(price) * 0.95
