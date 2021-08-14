from django.urls import path, re_path
import basketapp.views as basketapp

app_name = 'basketapp'

urlpatterns = [
    path('', basketapp.index, name='index'),
    re_path(r'^add/product/(?P<pk>\d+)/$', basketapp.add, name='add'),
    re_path(r'^delete/basket/position/(?P<pk>\d+)/$', basketapp.delete, name='delete'),
    path('edit/<int:pk>/<int:quantity>/', basketapp.basket_edit),
]
