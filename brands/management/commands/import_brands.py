import csv
from django.core.management.base import BaseCommand
from brands.models import Brand
from accounts.models import User


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '--filename',
            type=str,
            help='File type CSV with delimiter "|" to import brands'
        )

    def handle(self, *args, **options):
        filename = options['filename']
        self.stdout.write(f'Importing brands from {filename}')
        user = User.objects.filter(username='admin').first()

        if not user:
            self.stdout.write('Admin user not found')
            return

        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter='|')
            for row in reader:
                self.stdout.write(f'Importing brand {row["name"]}')
                brand = Brand(
                    name=row['name'],
                    description=row['description'],
                    user_created=user,
                    user_updated=user
                )

                try:
                    brand.save()
                    self.stdout.write(f'Brand {brand.name} saved successfully.')
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(
                            f'Error importing brand {brand.name}: {e}'
                        )
                    )

        self.stdout.write(
            self.style.SUCCESS('Brands imported successfully')
        )
