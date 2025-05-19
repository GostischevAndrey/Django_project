from django.db import models


class Category(models.Model):
    name_category = models.CharField(
        max_length=150,
        verbose_name="Наименование категории",
        help_text="Введите наименование категории",
    )
    descriptions = models.TextField(
        verbose_name="Описание категории", help_text="Введите описание категории"
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name_category


class Product(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Наименование продукта",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        verbose_name="Описание продукта", help_text="Введите описание продукта"
    )
    image = models.ImageField(
        blank=True, null=True, upload_to="product", help_text="Изображение"
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name
