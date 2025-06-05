from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.shortcuts import reverse
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "product_form.html"
    success_url = reverse_lazy("catalog:home")


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "product_form.html"

    def get_success_url(self):
        return reverse("catalog:product_info", args=[self.kwargs.get("pk")])


class ProductListView(ListView):
    model = Product
    template_name = "home.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_info.html"
    context_object_name = "product"


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "product_delete.html"
    success_url = reverse_lazy("catalog:home")


class ContactsView(TemplateView):
    template_name = "contacts.html"

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        return HttpResponse(f"Данные отправлены, {name}")
