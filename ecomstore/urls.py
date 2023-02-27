"""ecomstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.defaults import page_not_found


def custom_page_not_found(request):
    return page_not_found(request, None)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('preview.urls')),
    path('', include('catalog.urls')),
    path('cart/', include('cart.urls')),
    path('404/', custom_page_not_found),
    # (r'^accounts/', include('accounts'urls')),
    # (r'^accounts/', include('django.contrib.auth.urls')),
    # path('accounts/', include(accounts.urls)),
    # path('accounts/', include(django.contrib.auth.urls)),
]
