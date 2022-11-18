from django.contrib import admin
from django.urls import path
from stripe_api.views import (
    CreateCheckoutSessionView,
    ItemLandingPageView,
    SuccessView,
    CancelView,
    stripe_webhook
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('webhooks/stripe/', stripe_webhook, name='stripe-weghook'),
    path('', ItemLandingPageView.as_view(), name='landing-page'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session')
]
