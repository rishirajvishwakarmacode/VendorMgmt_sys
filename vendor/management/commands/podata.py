# your_app/management/commands/generate_purchase_order_data.py
from django.core.management.base import BaseCommand
from faker import Faker
import random
from vendor.models import Vendor, PurchaseOrder
import datetime

class Command(BaseCommand):
    help = 'Generates pseudo data for purchase orders'

    def handle(self, *args, **kwargs):
        faker = Faker()
        vendors = list(Vendor.objects.all())

        for _ in range(1000):
            vendor = random.choice(vendors)
            po_number = faker.unique.uuid4()
            order_date = faker.date_time_this_year()
            expected_delivery_date = faker.date_time_between(start_date=order_date, end_date='+30d')
            actual_delivery_date = faker.date_time_between(start_date=expected_delivery_date, end_date=expected_delivery_date + datetime.timedelta(days=10)) if random.random() < 0.7 else None
            items = [{"name": faker.word(), "price": faker.random_number(digits=3)} for _ in range(random.randint(1, 5))]
            quantity = sum(item['price'] for item in items)
            status = random.choice(['pending', 'completed', 'canceled'])
            quality_rating = random.uniform(0, 5) if status == 'completed' else None
            issue_date = faker.date_time_between(start_date=order_date - datetime.timedelta(days=10), end_date=order_date)
            acknowledgment_date = faker.date_time_between(start_date=issue_date, end_date=order_date) if status == 'completed' else None
            
            purchase_order = PurchaseOrder.objects.create(
                po_number=po_number,
                vendor=vendor,
                order_date=order_date,
                expected_delivery_date=expected_delivery_date,
                actual_delivery_date=actual_delivery_date,
                items=items,
                quantity=quantity,
                status=status,
                quality_rating=quality_rating,
                issue_date=issue_date,
                acknowledgment_date=acknowledgment_date
            )
            self.stdout.write(self.style.SUCCESS(f'Created purchase order: {purchase_order.po_number}'))
