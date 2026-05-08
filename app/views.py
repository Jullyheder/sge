import json
import re
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from markdown import markdown
from app.metrics import (
    get_products_metrics,
    get_sales_metrics,
    get_daily_sales_data,
    get_daily_sales_quantity_data,
    get_graphic_product_category_metric,
    get_graphic_product_brand_metric
)
from ai.models import AIResult


@login_required(login_url='login')
def home(request):
    product_metrics = get_products_metrics()
    sales_metrics = get_sales_metrics()
    daily_sales_data = get_daily_sales_data()
    daily_sales_quantity_data = get_daily_sales_quantity_data()
    graphic_product_category_metric = get_graphic_product_category_metric()
    graphic_product_brand_metric = get_graphic_product_brand_metric()
    ai_result = AIResult.objects.first().result

    context = {
        'product_metrics': product_metrics,
        'sales_metrics': sales_metrics,
        'daily_sales_data': json.dumps(daily_sales_data),
        'daily_sales_quantity_data': json.dumps(daily_sales_quantity_data),
        'product_count_by_category': json.dumps(graphic_product_category_metric),
        'product_count_by_brand': json.dumps(graphic_product_brand_metric),
        'ai_result': markdown(ai_result),
    }

    return render(request, 'home.html', context)
