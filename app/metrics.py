from django.db.models import Sum, F
from django.utils import timezone
from django.utils.formats import number_format
from products.models import Product
from outflows.models import Outflow
from categories.models import Category
from brands.models import Brand


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
        'total_cost_price': number_format(
            total_cost_price, decimal_pos=2, force_grouping=True
        ),
        'total_selling_price': number_format(
            total_selling_price, decimal_pos=2, force_grouping=True
        ),
        'total_profit': number_format(
            total_profit, decimal_pos=2, force_grouping=True
        )
    }

    return product_metrics


def get_sales_metrics() -> dict:
    outflows = Outflow.objects.all()
    total_sales = outflows.count()
    total_products_sold = outflows.aggregate(
        total_products_sold=Sum('quantity')
    )['total_products_sold'] or 0
    total_sales_value = sum(
        outflow.quantity * outflow.product.selling_price
        for outflow in outflows
    )
    total_sales_profit = sum(
        outflow.quantity * (outflow.product.selling_price - outflow.product.cost_price)
        for outflow in outflows
    )

    sales_metrics = {
        'total_sales': total_sales,
        'total_products_sold': total_products_sold,
        'total_sales_value': number_format(
            total_sales_value, decimal_pos=2, force_grouping=True
        ),
        'total_sales_profit': number_format(
            total_sales_profit, decimal_pos=2, force_grouping=True
        )
    }

    return sales_metrics


def get_daily_sales_data() -> dict:
    today = timezone.now().date()
    dates = [
        str(today - timezone.timedelta(days=i))
        for i in range(6, -1, -1)
    ]
    values = list()

    for date in dates:
        sales_total = Outflow.objects.filter(
            created_at__date=date
        ).aggregate(
            total_sales=Sum(F('quantity') * F('product__selling_price'))
        )['total_sales'] or 0
        values.append(float(sales_total))

    return {
        'dates': dates,
        'values': values
    }


def get_daily_sales_quantity_data() -> dict:
    today = timezone.now().date()
    dates = [
        str(today - timezone.timedelta(days=i))
        for i in range(6, -1, -1)
    ]
    quantities = list()

    for date in dates:
        sales_quantity = Outflow.objects.filter(
            created_at__date=date
        ).count()
        quantities.append(sales_quantity)

    return {
        'dates': dates,
        'values': quantities
    }


def get_graphic_product_category_metric():
    categories = Category.objects.all()
    category_metrics = dict()

    for category in categories:
        category_metrics[category.name] = category.products.count()

    return category_metrics


def get_graphic_product_brand_metric():
    brands = Brand.objects.all()
    brand_metrics = dict()

    for brand in brands:
        brand_metrics[brand.name] = brand.products.count()

    return brand_metrics
