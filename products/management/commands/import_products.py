import csv
import random
from django.core.management.base import BaseCommand
from products.models import Product
from accounts.models import User
from brands.models import Brand
from categories.models import Category


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '--filename',
            type=str,
            help='File type CSV with delimiter "|" to import products'
        )

    def handle(self, *args, **options):
        filename = options['filename']
        self.stdout.write(f'Importing products from {filename}')
        user = User.objects.filter(username='admin').first()

        if not user:
            self.stdout.write('Admin user not found')
            return

        brands = Brand.objects.all()
        categories = Category.objects.all()

        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter='|')
            for row in reader:
                self.stdout.write(f'Importing product {row["title"]}')
                product = Product(
                    title=row['title'],
                    brand=random.choice(brands),
                    category=random.choice(categories),
                    description=row['description'],
                    serie_number=row['serie_number'],
                    cost_price=row['cost_price'],
                    selling_price=row['selling_price'],
                    user_created=user,
                    user_updated=user
                )

                try:
                    product.save()
                    self.stdout.write(f'Product {product.title} saved successfully.')
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(
                            f'Error importing product {product.title}: {e}'
                        )
                    )

        self.stdout.write(
            self.style.SUCCESS('Products imported successfully')
        )
