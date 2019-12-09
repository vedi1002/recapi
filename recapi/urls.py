from django.urls import path
from recapi.views import ListProducts

urlpatterns = [
    path('',ListProducts.as_view(),name='get_products')
]