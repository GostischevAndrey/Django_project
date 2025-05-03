from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Add test students to the database"

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        category, _ = Category.objects.get_or_create(name_category="Категория 1")

        product = [
            {
                "name": "Телевизор",
                "descriptions": "",
                "category": category,
                "price": 500000,
                "image": "",
            },
            {
                "name": "Холодильник",
                "descriptions": "",
                "category": category,
                "price": 70000,
                "image": "",
            },
            {
                "name": "Самокат",
                "descriptions": "",
                "category": category,
                "price": 46000,
                "image": "",
            },
        ]

        for prod in product:
            product, created = Product.objects.get_or_create(**prod)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully added product: {product.name} {product.price}"
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"Product already exists: {product.name} {product.price}"
                    )
                )
