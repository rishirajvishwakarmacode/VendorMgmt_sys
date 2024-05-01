# admin.py
from django.contrib import admin
from .models import Vendor, Performance, PurchaseOrder

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['vendor_id','name', 'contact_details', 'address',
                    'on_time_delivery_rate', 'quality_rating_avg',
                    'average_response_time', 'fulfillment_rate']

@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ['vendor', 'date', 'on_time_delivery_rate',
                    'quality_rating_avg', 'average_response_time',
                    'fulfillment_rate']

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ['po_number', 'vendor', 'order_date', 'expected_delivery_date',
                    'actual_delivery_date', 'quantity', 'status', 'quality_rating',
                    'issue_date', 'acknowledgment_date']
