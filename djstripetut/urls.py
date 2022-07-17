from django.urls import path
from django.contrib import admin

from products.views import (
    CreateCheckoutSessionView,
    ProductLandingPageView,
    CancelView,
    SuccessView,
) 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductLandingPageView.as_view(), name='landing-page'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session')
    
]
