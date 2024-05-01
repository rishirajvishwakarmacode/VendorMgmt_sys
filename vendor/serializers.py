from rest_framework import serializers
from .models import *

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['vendor_id', 'name', 'contact_details', 'address', 
                  'on_time_delivery_rate', 'quality_rating_avg', 
                  'average_response_time', 'fulfillment_rate']

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = ['po_number', 'vendor', 'order_date', 'expected_delivery_date', 
                  'actual_delivery_date', 'items', 'quantity', 'status', 
                  'quality_rating', 'issue_date', 'acknowledgment_date']
        read_only_fields = ['po_number']

class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = ['id', 'vendor', 'date', 'on_time_delivery_rate', 
                  'quality_rating_avg', 'average_response_time', 'fulfillment_rate']
        read_only_fields = ['id']