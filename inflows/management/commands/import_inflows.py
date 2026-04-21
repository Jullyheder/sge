import csv
import random
from django.core.management.base import BaseCommand
from inflows.models import Inflow
from accounts.models import User
from suppliers.models import Supplier
from products.models import Product


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '--filename',
            type=str,
            help='File type CSV with delimiter "|" to import inflows'
        )

    def handle(self, *args, **options):
        filename = options['filename']
        self.stdout.write(f'Importing inflows from {filename}')
        user = User.objects.filter(username='admin').first()

        if not user:
            self.stdout.write('Admin user not found')
            return

        suppliers = Supplier.objects.all()
        products = Product.objects.all()

        with open(filename, 'r', encoding='utf-8') as file:
            reader = list(csv.DictReader(file, delimiter='|'))

            for i, product in enumerate(products):
                self.stdout.write(f'Importing inflow {product.title}')
                description = str()
                quantity = random.randint(1, 50)
                try:
                    row = reader[i]
                    description = row['description']
                    quantity = row['quantity']
                except IndexError:
                    self.stdout.write(
                        self.style.WARNING(
                            'No more descriptions to import, next product'
                        )
                    )

                inflow = Inflow(
                    supplier=random.choice(suppliers),
                    product=product,
                    quantity=int(quantity),
                    description=description,
                    user_created=user,
                    user_updated=user
                )

                try:
                    inflow.save()
                    self.stdout.write(f'Inflow {product.title} saved successfully.')
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(
                            f'Error importing inflow {product.title}: {e}'
                        )
                    )

        self.stdout.write(
            self.style.SUCCESS('Inflows imported successfully')
        )
