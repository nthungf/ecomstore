from django.urls import path

from cart import views

# urlpatterns = patterns('ecomstore.cart.views',
#                        (r'^$', 'show_cart', {'template_name': 'cart/cart.html'}, 'show_cart'),
#                        )

urlpatterns = [
    path('', views.show_cart, name="show_cart"),
]
