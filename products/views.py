from django.shortcuts import redirect, render
from django.views import View
from django.conf import settings
from django.http import JsonResponse
from django.views.generic import TemplateView
import stripe
from .models import Product, Price

stripe.api_key = settings.STRIPE_SECRET_KEY
# Create your views here.

class ProductLandingPageView(TemplateView):
    template_name = 'landing.html'

    def get_context_data(self, **kwargs):
        product = Product.objects.get(name="Test Product")
        prices = Price.objects.filter(product=product)
        context = super(ProductLandingPageView,
                        self).get_context_data(**kwargs)
        context.update({
            "product": product,
            "prices": prices
        })
        return context


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        YOUR_DOMAIN = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types = ['card'],
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': 'price_1LMXkWL3fwEVJEfhTcrd3fsG',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
            
        )
        
        return redirect(checkout_session.url)


class SuccessView(TemplateView):
    template_name = "success.html"

class CancelView(TemplateView):
    template_name = "cancel.html"
