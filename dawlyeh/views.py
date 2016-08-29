from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from forms import *


# from forms import RegistrationForm


def index(request):
    return render(request, 'dawlyeh/home.html')


def login(request):
    return render(request, 'dawlyeh/login.html')


def signup(request):
    return render(request, 'dawlyeh/signup.html')


def product_list(request):
    return render(request, 'dawlyeh/product-list-right-sidebar.html')


def product_grid(request):
    return render(request, 'dawlyeh/product-grid-right-sidebar.html')


def product_details(request):
    return render(request, 'dawlyeh/single-product.html')


def profile_dashboard(request):
    return render(request, 'dawlyeh/account-dashboard.html')


def profile_profile(request):
    return render(request, 'dawlyeh/account-profile.html')


def profile_address(request):
    return render(request, 'dawlyeh/account-address.html')


def profile_wishlist(request):
    return render(request, 'dawlyeh/account-wishlist.html')


def profile_order(request):
    return render(request, 'dawlyeh/account-all-orders.html')


def order_details(request):
    return render(request, 'dawlyeh/account-single-order.html')


def cart_details(request):
    return render(request, 'dawlyeh/cart-page.html')


def checkout_step1(request):
    return render(request, 'dawlyeh/checkout-step-1.html')


def checkout_step2(request):
    return render(request, 'dawlyeh/checkout-step-2.html')


def checkout_step3(request):
    return render(request, 'dawlyeh/checkout-step-3.html')


def checkout_step4(request):
    return render(request, 'dawlyeh/checkout-step-4.html')


def checkout_complete(request):
    return render(request, 'dawlyeh/checkout-complete.html')


def terms_conditions(request):
    return render(request, 'dawlyeh/terms-and-conditions.html')


def about_us(request):
    return render(request, 'dawlyeh/about-us.html')


def privacy_policy(request):
    return render(request, 'dawlyeh/privacy-policy.html')


def product_search(request):
    return render(request, 'dawlyeh/search_result.html')


def contact_us(request):
    form = ContactUsForm(request.POST or None)
    context = {
        'form': form,
    }

    if form.is_valid():
        form_name = form.cleaned_data.get('name')
        form_email = form.cleaned_data.get('email')
        form_message = form.cleaned_data.get('message')
        subject = "main Contact Us"
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, 'Ismaeelsameed@hotmail.com']
        contact_message = """
            %s : %s via %s
            """ % (form_name, form_message, form_email)
        html_message = """
            <h1>Contact Us Email</h1>
            <h3> %s </h3>
            <p><strong><u>Message: </u> %s </strong></p>
            <i> Via %s </i>
        """ % (form_name, form_message, form_email)

        send_mail(subject, contact_message, from_email, to_email, html_message=html_message, fail_silently=False)
    form = ContactUsForm()
    context = {
        'form': form,
    }
    return render(request, 'dawlyeh/contact_us.html', context)
