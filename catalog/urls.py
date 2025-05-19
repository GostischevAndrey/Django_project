from django.urls import path

from catalog.apps import CatalogConfig
from . import views
from .views import ContactsView

app_name = CatalogConfig.name

urlpatterns = [
    path("", views.ProductListView.as_view(), name="home"),
    path(
        "product_info/<int:pk>", views.ProductDetailView.as_view(), name="product_info"
    ),
    path("create/", views.ProductCreateView.as_view(), name="product_create"),
    path("update/<int:pk>", views.ProductUpdateView.as_view(), name="product_update"),
    path("delete/<int:pk>", views.ProductDeleteView.as_view(), name="product_delete"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
]
