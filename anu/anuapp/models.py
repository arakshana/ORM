from django.db import models
from django.contrib import admin

class DeliveryPartner(models.Model):
    partner_id =models.IntegerField()
    Name = models.CharField(max_length=50)
    dob =models.DateField()
    Email_id = models.EmailField()
    phoneno = models.IntegerField(primary_key=True)
    address = models.TextField()
    Rating_percentage = models.FloatField() 
class DetailsAdmin(admin.ModelAdmin):
    list_display=["partner_id","Name","dob","Email_id","phoneno","address","Rating_percentage"]

