import csv
import random
from django.core.management.base import BaseCommand
from outflows.models import Outflow
from accounts.models import User
from products.models import Product


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '--filename',
            type=str,
            help='File type CSV with delimiter "|" to import outflows'
        )

    def handle(self, *args, **options):
        filename = options['filename']
        self.stdout.write(f'Importing outflows from {filename}')
        user = User.objects.filter(username='admin').first()

        if not user:
            self.stdout.write('Admin user not found')
            return

        products = Product.objects.all()

        percentage_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

        with open(filename, 'r', encoding='utf-8') as file:
            reader = list(csv.DictReader(file, delimiter='|'))
            for i, product in enumerate(products):
                self.stdout.write(f'Importing outflow {product.title}')
                description = str()
                try:
                    row = reader[i]
                    description = row['description']
                except IndexError:
                    self.stdout.write(
                        self.style.WARNING(
                            'No more descriptions to import, next product'
                        )
                    )

                outflow = Outflow(
                    product=product,
                    quantity=round(random.choice(percentage_list) * product.quantity / 100),
                    description=description,
                    user_created=user,
                    user_updated=user
                )

                try:
                    outflow.save()
                    self.stdout.write(f'Outflow {product.title} saved successfully.')
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(
                            f'Error importing outflow {product.title}: {e}'
                        )
                    )

        self.stdout.write(
            self.style.SUCCESS('Outflows imported successfully')
        )
