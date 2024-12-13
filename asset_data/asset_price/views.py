# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import GoldPriceSerializer, AssetPriceSerializer
from .services import get_gold_price, get_asset_price

# Create your views here.
class GoldPriceView(APIView):
    def get(self, request):
        data = get_gold_price()
        if data:
            serializer = GoldPriceSerializer(data=data)
            if serializer.is_valid():
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        else:
            return Response({'error': 'Could not retrieve gold price data'}, status=500)

class AssetPriceView(APIView):
    def get(self, request, asset):
        data = get_asset_price(asset)
        if data:
            serializer = AssetPriceSerializer(data=data)
            if serializer.is_valid():
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        else:
            return Response({'error': f'Could not retrieve {asset} price data'}, status=500)

class AllAssetPriceView(APIView):
    def get(self, request):
        assets = ['XAU', 'XAG', 'BTC', 'ETH']
        data = {}
        for asset in assets:
            data[asset] = get_asset_price(asset)
        return Response(data)