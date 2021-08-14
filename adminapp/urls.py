from django.urls import path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.UserList.as_view(), name='index'),
    path('user/create/', adminapp.user_create, name='user_create'),
    path('user/<int:pk>/update/', adminapp.user_update, name='user_update'),
    path('user/<int:pk>/delete/', adminapp.user_delete, name='user_delete'),
    path('user/<int:pk>/recover/', adminapp.user_recover, name='user_recover'),
    path('categories/', adminapp.ProductCategoriesList.as_view(), name='categories'),
    path('categories/category/create/', adminapp.ProductCategoryCreate.as_view(), name='category_create'),
    path('categories/category/<int:pk>/update/', adminapp.ProductCategoryUpdate.as_view(), name='category_update'),
    path('categories/category/<int:pk>/delete/', adminapp.ProductCategoryDelete.as_view(), name='category_delete'),
    path('categories/category/<int:pk>/recover/', adminapp.category_recover, name='category_recover'),
    # path('categories/product/', adminapp.ProductList.as_view(), name='product'),
    # path('categories/product/create/', adminapp.ProductCreate.as_view(), name='product_create'),
    path('categories/<int:category_pk>/product/create/', adminapp.product_create, name='product_create'),
    path('categories/product/<int:category_pk>/', adminapp.products_in_category, name='products_in_category'),
    path('categories/product/<int:pk>/update/', adminapp.ProductUpdate.as_view(), name='product_update'),
    path('categories/product/<int:pk>/delete/', adminapp.ProductDelete.as_view(), name='product_delete'),
    path('categories/product/<int:pk>/recover/', adminapp.product_recover, name='product_recover'),
]
