from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AuctionSerializer
from .models import Auction


# Create your views here.


class AuctionViewSet(viewsets.ModelViewSet):
    serializer_class = AuctionSerializer
    queryset = Auction.objects.all()
