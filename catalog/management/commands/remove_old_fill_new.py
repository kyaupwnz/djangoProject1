from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = [
            {'category_name': 'Конфеты', 'description': 'Сладости и радости'},
            {'category_name': 'Алкогольная продукция', 'description': 'Алкогольная продукция'}
        ]
        products = [
            {'product_name': 'йогурт', 'unit_price': '70', 'description': 'Вкусный йогурт','category.category_name': 'Молочная продукция', 'date_of_last_changes': '2023-01-19'  }
        ]
        product_list = []
        category_list = []
        for item in products:
            product_list.append(Product(**item))

        for item in categories:
            category_list.append(Category(**item))

        Product.objects.all().delete()
        Product.objects.bulk_create(product_list)

        Category.objects.all().delete()
        Category.objects.bulk_create(category_list)

