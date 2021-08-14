from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse

# Create your views here.
from django.template import loader
from django.template.loader import render_to_string
from django.urls import reverse

from basketapp.models import BasketPosition
from mainapp.models import Product


@login_required
def index(request):
    basket_positions = request.user.basketposition_set.all()
    context = {
        'title_page': 'корзина',
        'basket_positions': basket_positions,
    }

    return render(request, 'basketapp/index.html', context)


@login_required
def add(request, pk):
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(
            reverse(
                'main:page_product',
                kwargs={'pk': pk}
            )
        )
    product = get_object_or_404(Product, pk=pk)
    basket = request.user.basketposition_set.filter(product=pk).first()

    if not basket:
        basket = BasketPosition(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def delete(request, pk):
    get_object_or_404(BasketPosition, pk=pk).delete()
    return HttpResponseRedirect(reverse('basket:index'))


@login_required
def basket_edit(request, pk, quantity):
    if request.is_ajax():
        quanty = int(quantity)
        new_basket_item = BasketPosition.objects.filter(pk=int(pk)).first()

        if quanty > 0:
            new_basket_item.quantity = quanty
            new_basket_item.save()
        else:
            new_basket_item.delete()

        basket_positions = BasketPosition.objects.filter(user=request.user)

        context = {
            'basket_positions': basket_positions,
        }

        result = loader.render_to_string(
            'basketapp/includes/inc__basket_items.html',
            context=context,
            request=request,
        )

        return JsonResponse({
            'result': result,
        })
