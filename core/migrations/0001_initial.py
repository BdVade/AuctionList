# Generated by Django 4.0.4 on 2022-05-28 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('top_bid', models.IntegerField()),
                ('top_bidder', models.CharField(max_length=200)),
                ('auction_info', models.CharField(max_length=200)),
                ('floor_price', models.IntegerField()),
            ],
        ),
    ]
