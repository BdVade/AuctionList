from django.db import models

# Create your models here.


class Auction(models.Model):
    name = models.CharField(max_length=40)
    top_bid = models.IntegerField()
    top_bidder = models.CharField(max_length=200)
    auction_info = models.CharField(max_length=200)
    floor_price = models.IntegerField()
