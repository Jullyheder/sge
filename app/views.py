from django.shortcuts import render
from app.metrics import get_products_metrics


def home(request):
    product_metrics = get_products_metrics()

    context = {
        'product_metrics': product_metrics
    }

    return render(request, 'home.html', context)
