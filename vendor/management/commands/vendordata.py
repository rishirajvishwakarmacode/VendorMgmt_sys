# your_app/management/commands/generate_vendor_data.py
from django.core.management.base import BaseCommand
from faker import Faker
from vendor.models import Vendor

class Command(BaseCommand):
    help = 'Generates pseudo data for 10 vendor profiles'

    def handle(self, *args, **kwargs):
        faker = Faker()

        for _ in range(10):
            vendor = Vendor.objects.create(
                vendor_id=faker.unique.random_number(digits=5),
                name=faker.company(),
                contact_details=faker.phone_number(),
                address=faker.address(),
                on_time_delivery_rate=faker.pyfloat(left_digits=2, right_digits=2, positive=True),
                quality_rating_avg=faker.pyfloat(left_digits=2, right_digits=2, positive=True),
                average_response_time=faker.pyfloat(left_digits=2, right_digits=2, positive=True),
                fulfillment_rate=faker.pyfloat(left_digits=2, right_digits=2, positive=True)
            )
            self.stdout.write(self.style.SUCCESS(f'Created vendor: {vendor.name}'))
