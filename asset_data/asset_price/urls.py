from django.urls import path
from .views import GoldPriceView, AssetPriceView, AllAssetPriceView

urlpatterns = [
    path('gold-price/', GoldPriceView.as_view(), name='gold_price'),
    path('asset-price/', AllAssetPriceView.as_view(), name='all_asset_price'),
    path('asset-price/<str:asset>/', AssetPriceView.as_view(), name='asset_price'),
]