from django.urls import path
from balance.views import fetch_balance

urlpatterns = [
    path('', fetch_balance, name='fetch_balance'),
]
