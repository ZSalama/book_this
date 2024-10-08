from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from subscriptions.models import SubscriptionPrice
import helpers.billing
from django.urls import reverse
from django.conf import settings

BASE_URL = settings.BASE_URL
# Create your views here.
def product_price_redirect_view(request, price_id=None, *args, **kwargs):
    request.session['checkout_subscription_price_id']=price_id
    return redirect("stripe-checkout-start")

@login_required
def checkout_redirect_view(request):
    checkout_subscription_price_id = request.session.get("checkout_subscription_price_id")
    try:
        obj = SubscriptionPrice.objects.get
    except:
        obj = None
    if checkout_subscription_price_id is None or obj is None:
        return redirect('pricing')
    
    customer_stripe_id = request.user.customer.stripe_id
    success_url_path = reverse("stripe-checkout-end")
    success_url = f"{BASE_URL}{success_url_path}"
    pricing_url_path = reverse("pricing")
    return_url= f"{BASE_URL}{pricing_url_path}"
    price_stripe_id = obj.stripe_id

    url = helpers.billing.start_checkout_session(
        customer_stripe_id,
        success_url=success_url,
        return_url=return_url,
        price_stripe_id=price_stripe_id,
        raw=False
    )
    return redirect(url)

def checkout_finalize_view(request):
    return