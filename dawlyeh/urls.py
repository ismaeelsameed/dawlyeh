from django.conf.urls import include, url
from views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'main.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index, name='index'),
    # PRODUCT URLS ##
    # PTODUCT LIST & GRID ##
    url(r'^products_list/$', product_list, name='product_list'),
    url(r'^products_grid/$', product_grid, name='product_grid'),

    # PRODUCT DETAIL
    url(r'^products/slug/$', product_details, name='product_detail'),

    # MY ACCOUNT URLS
    # MY DASHBOARD
    url(r'^profile/dashboard/$', profile_dashboard, name='my_dashboard'),
    # MY PROFILE
    url(r'^profile/profile/$', profile_profile, name='my_profile'),
    # MY ACCOUNT
    url(r'^profile/address/$', profile_address, name='my_address'),
    # MY WISHLIST
    url(r'^profile/wishlist/$', profile_wishlist, name='my_wishlist'),

    # MY ORDERS
    url(r'^profile/orders/$', profile_order, name='my_orders'),

    # ORDER DETAILS
    url(r'^profile/orders/slug$', order_details, name='order_detail'),

    # CART DETAILS
    url(r'^cart/', cart_details, name='cart_details'),

    # CHECKOUT
    url(r'^checkout_step1/', checkout_step1, name='checkout_step1'),
    url(r'^checkout_step2/', checkout_step2, name='checkout_step2'),
    url(r'^checkout_step3/', checkout_step3, name='checkout_step3'),
    url(r'^checkout_step4/', checkout_step4, name='checkout_step4'),
    url(r'^checkout_complete/', checkout_complete, name='checkout_complete'),

    # LOGIN
    url(r'^login/', login, name='login'),
    # SIGN UP
    url(r'^signup/', signup, name='signup'),

    # TERMS & CONDITIONS
    url(r'^terms_conditions/', terms_conditions, name='terms_conditions'),

    # ABOUT US
    url(r'^about_us/', about_us, name='about_us'),

    # PRIVACY POLICY
    url(r'^privacy_policy/', privacy_policy, name='privacy_policy'),

    # PRODUCTS SEARCH
    url(r'^search/$', product_search, name='product_search'),

    # CONTACT US
    url(r'^contact_us/$', contact_us, name='contact_us'),
]
