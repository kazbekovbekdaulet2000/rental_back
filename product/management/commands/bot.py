from django.core.management.base import BaseCommand
from product.management.commands.run_pooling import run_pooling
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rental_back.settings')
django.setup()


class Command(BaseCommand):
    help = "Запускает бота"

    def handle(self, *args, **options):
        run_pooling()
