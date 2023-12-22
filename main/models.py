from django.db import models

# Create your models here.

STATUS_CHOICES = (
    ('pending','pending'),
    ('completed','completed'),
    ('canceled','canceled'),
)

class Vendor(models.Model):
    name =  models.CharField(max_length = 100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length = 100, unique=True) 
    on_time_delivery_rate = models.FloatField(null = False) 
    quality_rating_avg = models.FloatField(null = False)
    average_response_time = models.FloatField(null = False)
    fulfillment_rate = models.FloatField(null = False)

    


class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length = 100, unique=True)  
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    delivered_on_time = models.BooleanField(default = False)
    items = models.JSONField()
    quantity = models.IntegerField() 
    status = models.CharField(default ='pending',choices=STATUS_CHOICES, max_length = 40)
    quality_rating = models.FloatField(null = True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null = True , blank=True)

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    date =  models.DateTimeField(auto_now_add=True) 
    on_time_delivery_rate = models.FloatField(null=True)
    quality_rating_avg = models.FloatField(null=True)
    average_response_time = models.FloatField(null=True)
    fulfillment_rate = models.FloatField(null=True)
