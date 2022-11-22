from django.contrib import admin
from django.urls import path
from stripe_api.views import (
    CreateCheckoutSessionView,
    ItemLandingPageView,
    SuccessView,
    CancelView,
    HomeView,

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    # path('webhooks/stripe/', stripe_webhook, name='stripe-weghook'),
    path('item/<pk>/', ItemLandingPageView.as_view(), name='item'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('buy/<pk>/', CreateCheckoutSessionView.as_view(), name='buy')
]
