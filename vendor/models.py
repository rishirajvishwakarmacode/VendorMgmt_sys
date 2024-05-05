from django.db import models
from django.db.models import F
import datetime
from django.db.models.signals import post_save, post_delete
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
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name="purchase_order")
    order_date = models.DateTimeField()
    expected_delivery_date = models.DateTimeField()
    actual_delivery_date = models.DateTimeField(null=True)
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=100)
    quality_rating = models.FloatField(null=True, default=0)
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
    
    def calculate_on_time_delivery_rate(self):
        completed_orders = self.vendor.purchase_order.filter(status = 'completed')
        on_time_orders = completed_orders.filter(actual_delivery_date__lte=F('expected_delivery_date'))

        total_completed_orders = completed_orders.count()
        print(total_completed_orders)
        print(on_time_orders.count())
        if total_completed_orders > 0:
            rate = on_time_orders.count()/total_completed_orders
            print(rate)
        else:
            rate = 0
        self.on_time_delivery_rate = rate
        self.save()

    def calculate_quality_rating_avg(self):
        completed_orders = self.vendor.purchase_order.filter(status = 'completed')
        ratings = completed_orders.values('quality_rating')
        print("Rating")
        print(ratings)
        sum=0
        for rating in ratings:
            sum += rating['quality_rating']
        avg = sum/ratings.count()
        print(avg)
        self.quality_rating_avg =  avg
        self.save()

    def calculate_fulfilment_rate(self):
        all_orders = self.vendor.purchase_order.all().count()
        print(all_orders)
        completed_orders = self.vendor.purchase_order.filter(status='completed').count()
        print(completed_orders)
        rate = completed_orders/all_orders
        print('Fulfillment_Rate')
        print(rate)
        self.fulfillment_rate = rate
        self.save()
    
    def calculate_response_time(self):
        all_orders = self.vendor.purchase_order.all()
        response_tlist = []
        for order in all_orders:
            if order.acknowledgment_date:
                response_time = order.acknowledgment_date - order.issue_date
                response_tlist.append(response_time.total_seconds()/3600)
        print(response_tlist)
        if response_tlist:
            ang = sum(response_tlist)/len(response_tlist)
        else:
            ang = 0
        print('average_response_time')
        print(ang)
        self.average_response_time = ang
        self.save()


@receiver([post_save, post_delete], sender=PurchaseOrder)
def update_performance(sender, instance, **kwargs):
    vendor = instance.vendor
    performance = Performance.objects.filter(vendor=vendor).first()
    performance.calculate_on_time_delivery_rate()
    performance.calculate_quality_rating_avg()
    performance.calculate_fulfilment_rate()
    performance.calculate_response_time()
