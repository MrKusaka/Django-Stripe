import stripe

from django.conf import settings
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.views import View
from .models import Item


stripe.api_key = settings.STRIPE_SECRET_KEY


class HomeView(TemplateView):
    template_name = "stripe_api/home.html"

    def get_context_data(self, **kwargs):
        return {'products': Item.objects.all()}


class SuccessView(TemplateView):
    template_name = "stripe_api/success.html"


class CancelView(TemplateView):
    template_name = "stripe_api/cancel.html"


class ItemLandingPageView(TemplateView):
    template_name = "stripe_api/landing.html"

    def get_context_data(self, **kwargs):
        item_id = self.kwargs["pk"]
        item = Item.objects.get(id=item_id)
        context = super(ItemLandingPageView, self).get_context_data(**kwargs)
        context.update({
            "product": item,
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
        })
        return context


class CreateCheckoutSessionView(View):
    def get(self, request, *args, **kwargs):
        product_id = self.kwargs["pk"]
        product = Item.objects.get(id=product_id)
        print(product)
        YOUR_DOMAIN = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': product.price,
                        'product_data': {
                            'name': product.name
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return JsonResponse({
            'id': checkout_session.id
        })
