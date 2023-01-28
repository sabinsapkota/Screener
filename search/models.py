from django.db import models
from datetime import datetime



# Create your models here.
class Crypto(models.Model):
    symbol = models.CharField(max_length=10)
    trend = models.CharField(max_length=25,null = True)
    price1 = models.FloatField(blank=True, null=True)
    price2 = models.FloatField(blank=True, null=True)
    price3 = models.FloatField(blank=True, null=True)
    price4 = models.FloatField(blank=True, null=True)
    price5 = models.FloatField(blank=True, null=True)
    price6 = models.FloatField()
    
    def save(self, *args, **kwargs):
     if float(self.price6)>float(self.price5)>float(self.price4) >float(self.price3):
      self.trend = "3star"
     if float(self.price6)>float(self.price5) >float(self.price4) >float(self.price3) >float(self.price2):
      self.trend = "4star"
     if float(self.price6)>float(self.price5) >float(self.price4) >float(self.price3) >float(self.price2)>float(self.price1):
      self.trend = "5star"
     else:
        self.trend = "Bearish"
     super(Crypto, self).save(*args, **kwargs) # Call the "real" save() method.
 
    def __str__(self):
     return f"{self.symbol}"

