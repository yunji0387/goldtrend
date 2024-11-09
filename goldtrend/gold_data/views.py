# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import GoldPriceSerializer
from .services import get_gold_price

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