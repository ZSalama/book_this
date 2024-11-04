from django.http import HttpResponseForbidden
from functools import wraps
from subscriptions.models import UserSubscription
from django.shortcuts import render

def active_subscription_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        try:
            user_subscription = UserSubscription.objects.get(user=request.user)
            if user_subscription.status == 'active':
                return view_func(request, *args, **kwargs)
            else:
                # Return the rendered template for inactive subscription
                return render(request, 'dashboard/active_sub_required.html', {})
        except UserSubscription.DoesNotExist:
            # Return the rendered template for no subscription
            return render(request, 'dashboard/active_sub_required.html', {})
    
    return _wrapped_view  # Return the wrapped view function