
from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views
from django.conf import settings#for photo upload
from django.conf.urls.static import static#for photo upload

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^admin/', include(admin.site.urls)),

    url(r'^reset/password_reset/$', 'django.contrib.auth.views.password_reset', name='reset_password_reset1'),
    url(r'^reset/password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
    url(r'^about$','book.views.about', name='about'),
    url(r'^contact$','book.views.contact', name='contact'),
    url(r'^condition$','book.views.condition', name='condition'),
    url(r'^users/add$','book.views.add_user', name='adduser'),
    url(r'^products/add/$','book.views.add_product', name='addproduct'),
    url(r'^products/del/$','book.views.del_product', name='delproduct'),
    url(r'^users/home/$','book.views.user_home', name='userhome'),
    url(r'^products/details/(?P<products_id>\d+)/$','book.views.details', name='details'),
    url(r'^products/home/(?P<catagory_id>\d+)/$','book.views.products_home', name='productshome'),
    url(r'^catagory/add/$','book.views.add_catagory', name='addcatagory'),
    url(r'^catagory/del/$','book.views.del_catagory', name='delcatagory'),
    url(r'^users/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^users/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'home.html'}),
    url(r'^users/account/$','book.views.user_account', name='useraccount'),
    url(r'^change/password/$','book.views.change_password', name='changepassword'),
    url(r'^users/profile/$','book.views.profile_update', name='profileupdate'),
    url(r'^users/cart/$','book.views.my_cart', name='mycart'),
    url(r'^order/cancel/$','book.views.cancel_order', name='cancelorder'),
    url(r'^products/delivary/$','book.views.products_delivery', name='productsdelivery'),
    url(r'^personal/details/$','book.views.personal_details', name='personaldetails'),





) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#for photo upload
