from django.urls import path

from catalog import views

# urlpatterns = patterns('ecomstore.catalog.views',
#                        (r'^$', 'index', {'template_name': 'catalog/index.html'}, 'catalog_home'),
#                        (r'^category/(?P<category_slug>[-\w]+)/$', 'show_category',
#                         {'template_name': 'catalog/category.html'}, 'catalog_category'),
#                        (r'^product/(?P<product_slug>[-\w]+)/$', 'show_product',
#                         {'template_name': 'catalog/product.html'}, 'catalog_product'), )

urlpatterns = [
    # path('catalog/', views.home, name='home'),
    path('catalog/', views.index, name="catalog_home"),
    path('category/<slug:category_slug>/', views.show_category, name="catalog_category"),
    path('product/<slug:product_slug>/', views.show_product, name="catalog_product"),
]
