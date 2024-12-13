from django.urls import path
from .views import GoldPriceView, AssetPriceView

urlpatterns = [
    path('gold-price/', GoldPriceView.as_view(), name='gold_price'),
    path('asset-price/<str:asset>/', AssetPriceView.as_view(), name='asset_price'),
]