from django.db import models

# Create your models here.

class Bank(models.Model):
    name = models.CharField(max_length=30)
    branch_count = models.PositiveSmallIntegerField(default=0)
    usd_buy = models.FloatField(null=True)
    usd_sell = models.FloatField(null=True)
    euro_buy = models.FloatField(null=True)
    euro_sell = models.FloatField(null=True)
    rub_buy = models.FloatField(null=True)
    rub_sell = models.FloatField(null=True)

    def __str__(self):
        return self.name