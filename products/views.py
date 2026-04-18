from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView
)
from products.models import Product
from products.forms import ProductForm


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.GET.get('title')
        if title:
            queryset = queryset.filter(title__icontains=title)

        return queryset


class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_create.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        product = form.save(commit=False)
        product.user_created = self.request.user
        product.user_updated = self.request.user
        return super().form_valid(form)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product_update.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        product = form.save(commit=False)
        product.user_updated = self.request.user
        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('product_list')
