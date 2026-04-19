import csv
from django.core.management.base import BaseCommand
from suppliers.models import Supplier
from accounts.models import User


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '--filename',
            type=str,
            help='File type CSV with delimiter "|" to import suppliers'
        )

    def handle(self, *args, **options):
        filename = options['filename']
        self.stdout.write(f'Importing suppliers from {filename}')
        user = User.objects.filter(username='admin').first()

        if not user:
            self.stdout.write('Admin user not found')
            return

        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter='|')
            for row in reader:
                self.stdout.write(f'Importing supplier {row["name"]}')
                supplier = Supplier(
                    name=row['name'],
                    description=row['description'],
                    user_created=user,
                    user_updated=user
                )

                try:
                    supplier.save()
                    self.stdout.write(f'Supplier {supplier.name} saved successfully.')
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(
                            f'Error importing supplier {supplier.name}: {e}'
                        )
                    )

        self.stdout.write(
            self.style.SUCCESS('Suppliers imported successfully')
        )
