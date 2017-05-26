"""secretgarden URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from store import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.homepage, name='index'),
    url(r'^homepage/',views.homepage, name='homepage'),
    url(r'^signin/',views.signin, name='signin'),
    url(r'^register/',views.register, name='register'),
    url(r'^productlist/(?P<menutype>\w+)/',views.menuproduct, name='menutype'),
    url(r'^signout/',views.signout, name='signout'),
    url(r'^productdetails/(?P<productID>\d+)/',views.productdetails, name='productID'),
    url(r'^shoppingcart/', views.cart_detail, name='cart_detail'),
    url(r'^viewshoppingcart/', views.cart_detail, name='viewshoppingcart'),
    url(r'^add/(?P<productID>\d+)/',views.cart_add,name='cart_add'),
    url(r'^addUpdate/(?P<productID>\d+)/(?P<price>\d+\.\d{2})$',views.cart_add_from_detail,name='cart_update'),
    url(r'^remove/(?P<productID>\d+)/', views.cart_remove,name='cart_remove'),
    url(r'^create/',views.order_create, name='order_create'),
    url(r'^paypal/',include('paypal.standard.ipn.urls')),
    url(r'^payment/',include('payment.urls',namespace='payment')),
]

#Setup static and media URLs 
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

