from django.db import models
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver

STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    )

class Vendor(models.Model):
    vendor_id = models.CharField(max_length=15, unique=True, primary_key=True)
    name = models.CharField(max_length=50)
    contact_details = models.TextField()
    address = models.TextField()
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
    
class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=100, primary_key=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    expected_delivery_date = models.DateTimeField()
    actual_delivery_date = models.DateTimeField(null=True)
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=100)
    quality_rating = models.FloatField(null=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.po_number
    

class Performance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField(default=True)
    quality_rating_avg = models.FloatField(default=True)
    average_response_time = models.FloatField(default=True)
    fulfillment_rate = models.FloatField(default=True)

    def __str__(self):
        return f"Performance record for {self.vendor.name} on {self.date}"

@receiver(post_save, sender=Performance)
def update_vendor_performance(sender, instance, created, **kwargs):
    if not created:  
        vendor = instance.vendor
        vendor.on_time_delivery_rate = instance.on_time_delivery_rate
        vendor.quality_rating_avg = instance.quality_rating_avg
        vendor.average_response_time = instance.average_response_time
        vendor.fulfillment_rate = instance.fulfillment_rate
        vendor.save()