from django.http import HttpResponseForbidden
from functools import wraps
from subscriptions.models import UserSubscription

def active_subscription_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        try:
            user_subscription = UserSubscription.objects.get(user=request.user)
            if user_subscription.status == 'active':
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseForbidden("You need an active subscription to access this page.")
        except UserSubscription.DoesNotExist:
            return HttpResponseForbidden("You need an active subscription to access this page.")
    return _wrapped_view