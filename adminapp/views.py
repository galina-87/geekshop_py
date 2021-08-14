from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from adminapp.forms import AdminShopUserCreateForm, AdminShopUserUpdateForm, AdminProductCategoryCreateForm, \
    AdminProductCreateForm
from mainapp.models import CategoryProduct, Product


# @user_passes_test(lambda x: x.is_superuser)
# def index(request):
#     users_list = get_user_model().objects.all().order_by(
#         '-is_active', '-is_superuser', '-is_staff', 'username'
#     )
#
#     context = {
#         'page_title': 'администрирование/пользователи',
#         'users_list': users_list,
#     }
#     return render(request, 'authapp/shopuser_list.html', context)

class OnlySuperUserMixin:
    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class TitlePageMixin:
    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(object_list=None, **kwargs)
        data['page_title'] = self.page_title
        return data


class UserList(OnlySuperUserMixin, TitlePageMixin, ListView):
    page_title = 'админка/пользователи'
    model = get_user_model()


@user_passes_test(lambda x: x.is_superuser)
def user_create(request):
    if request.method == 'POST':
        user_form = AdminShopUserCreateForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('adminapp:index'))
    else:
        user_form = AdminShopUserCreateForm()

    context = {
        'page_title': 'пользователь/создание',
        'user_form': user_form,
    }
    return render(request, 'adminapp/user_update.html', context)


class ProductCategoriesList(OnlySuperUserMixin, TitlePageMixin, ListView):
    page_title = 'админка/категории'
    model = CategoryProduct
    # paginate_by = 5


# class ProductList(OnlySuperUserMixin, TitlePageMixin, ListView):
#     page_title = 'админка/продукты'
#     model = Product

@user_passes_test(lambda x: x.is_superuser)
def products_in_category(request, category_pk):
    category = get_object_or_404(CategoryProduct, pk=category_pk)
    object_list = category.product_set.all()
    context = {
        'page_title': f'категория {category.name}/продукты',
        'category': category,
        'object_list': object_list,
    }
    return render(request, 'adminapp/category_products_list.html', context)


@user_passes_test(lambda x: x.is_superuser)
def user_update(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    if request.method == 'POST':
        user_form = AdminShopUserUpdateForm(request.POST, request.FILES, instance=user)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('adminapp:index'))
    else:
        user_form = AdminShopUserUpdateForm(instance=user)

    context = {
        'page_title': 'пользователь/редактирование',
        'user_form': user_form,
    }
    return render(request, 'adminapp/user_update.html', context)


@user_passes_test(lambda x: x.is_superuser)
def user_delete(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    if request.method == 'POST':
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('adminapp:index'))
    else:
        context = {
            'page_title': 'пользователь/удаление',
            'user_to_delete': user,
        }
        return render(request, 'adminapp/user_delete.html', context)


@user_passes_test(lambda x: x.is_superuser)
def user_recover(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    user.is_active = True
    user.save()
    return HttpResponseRedirect(reverse('adminapp:index'))


class ProductCategoryCreate(OnlySuperUserMixin, TitlePageMixin, CreateView):
    page_title = 'админка/категории/создание'
    model = CategoryProduct
    success_url = reverse_lazy('adminapp:categories')
    # fields = '__all__'
    form_class = AdminProductCategoryCreateForm


class ProductCategoryUpdate(OnlySuperUserMixin, TitlePageMixin, UpdateView):
    page_title = 'админка/категории/редактирование'
    model = CategoryProduct
    success_url = reverse_lazy('adminapp:categories')
    # fields = '__all__'
    form_class = AdminProductCategoryCreateForm


class ProductCategoryDelete(OnlySuperUserMixin, TitlePageMixin, DeleteView):
    page_title = 'админка/категории/удаление'
    model = CategoryProduct
    success_url = reverse_lazy('adminapp:categories')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


@user_passes_test(lambda x: x.is_superuser)
def category_recover(request, pk):
    category = get_object_or_404(CategoryProduct, pk=pk)
    category.is_active = True
    category.save()
    return HttpResponseRedirect(reverse('adminapp:categories'))


# class ProductCreate(OnlySuperUserMixin, TitlePageMixin, CreateView):
#     page_title = 'админка/продукт/создание'
#     model = Product
#     success_url = reverse_lazy('adminapp:product')
#     # fields = '__all__'
#     form_class = AdminProductCreateForm

@user_passes_test(lambda u: u.is_superuser)
def product_create(request, category_pk):
    category = get_object_or_404(CategoryProduct, pk=category_pk)
    if request.method == 'POST':
        form = AdminProductCreateForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(
                'adminapp:products_in_category',
                # 'adminapp:categories',
                kwargs={'category_pk': category.pk}
            ))
    else:
        form = AdminProductCreateForm(
            initial={
                'category': category,
            }
        )

    context = {
        'page_title': 'продукты/создание',
        'form': form,
        'category': category,
    }
    return render(request, 'adminapp/product_update.html', context)


class ProductUpdate(OnlySuperUserMixin, TitlePageMixin, UpdateView):
    page_title = 'админка/продукт/редактирование'
    model = Product
    success_url = reverse_lazy('adminapp:categories')
    # fields = '__all__'
    form_class = AdminProductCreateForm


class ProductDelete(OnlySuperUserMixin, TitlePageMixin, DeleteView):
    page_title = 'админка/продукт/удаление'
    model = Product

    # success_url = reverse_lazy('adminapp:products_in_category', kwargs={'category_pk': get_object().category.pk})

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(
            reverse('adminapp:products_in_category', kwargs={'category_pk': self.object.category.pk}))


@user_passes_test(lambda x: x.is_superuser)
def product_recover(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.is_active = True
    product.save()
    return HttpResponseRedirect(reverse('adminapp:products_in_category', kwargs={'category_pk': product.category.pk}))
