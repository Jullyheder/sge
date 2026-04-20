from django.utils.numberformat import format
from products.models import Product


def get_products_metrics() -> dict:
    products = Product.objects.all()
    total_quantity = sum(
        product.quantity for product in products
    )
    total_cost_price = sum(
        product.cost_price * product.quantity for product in products
    )
    total_selling_price = sum(
        product.selling_price * product.quantity for product in products
    )
    total_profit = total_selling_price - total_cost_price

    product_metrics = {
        'total_quantity': total_quantity,
        'total_cost_price': format(
            total_cost_price, decimal_pos=2, decimal_sep=',',
            thousand_sep='.', grouping=3, force_grouping=True
        ),
        'total_selling_price': format(
            total_selling_price, decimal_pos=2, decimal_sep=',',
            thousand_sep='.', grouping=3, force_grouping=True
        ),
        'total_profit': format(
            total_profit, decimal_pos=2, decimal_sep=',',
            thousand_sep='.', grouping=3, force_grouping=True
        )
    }

    return product_metrics
