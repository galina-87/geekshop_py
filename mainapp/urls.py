from django.urls import path, re_path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('catalog/', mainapp.catalog, name='catalog'),
    re_path(r'^products/category/(?P<pk>\d+)/$', mainapp.prodcat, name='products'),
    re_path(r'^products/category/(?P<pk>\d+)/page/(?P<page>\d+)$', mainapp.prodcat, name='products_page'),
    re_path(r'^product/(?P<pk>\d+)$', mainapp.page_product, name='page_product'),
    path('contact/', mainapp.contact, name='contact'),
]