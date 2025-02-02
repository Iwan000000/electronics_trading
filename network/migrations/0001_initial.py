# Generated by Django 5.0.4 on 2024-06-13 12:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="NetworkUnit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=500, verbose_name="название")),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("FA", "Завод"),
                            ("RN", "Розничная сеть"),
                            ("IE", "Индивидуальный предприниматель"),
                        ],
                        max_length=30,
                        verbose_name="тип звена сети",
                    ),
                ),
                (
                    "level",
                    models.CharField(
                        choices=[
                            ("0", "Нулевой уровень"),
                            ("1", "Первый уровень"),
                            ("2", "Второй уровень"),
                        ],
                        max_length=15,
                        verbose_name="уровень в иерархии поставок",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, null=True, verbose_name="email"
                    ),
                ),
                (
                    "country",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="страна"
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="город"
                    ),
                ),
                (
                    "street",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="улица"
                    ),
                ),
                (
                    "house_number",
                    models.CharField(
                        blank=True, max_length=15, null=True, verbose_name="номер дома"
                    ),
                ),
                (
                    "debt",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=10,
                        verbose_name="задолженность перед поставщиком",
                    ),
                ),
                (
                    "date_create",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="время создания"
                    ),
                ),
                (
                    "supplier",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="supplied_units",
                        to="network.networkunit",
                        verbose_name="ссылка на поставщика",
                    ),
                ),
            ],
            options={
                "verbose_name": "объект сети",
                "verbose_name_plural": "объекты сети",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150, verbose_name="название")),
                (
                    "model",
                    models.CharField(
                        blank=True, max_length=150, null=True, verbose_name="модель"
                    ),
                ),
                (
                    "release_date",
                    models.DateField(
                        blank=True,
                        null=True,
                        verbose_name="дата выхода продукта на рынок",
                    ),
                ),
                (
                    "network_unit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="network.networkunit",
                        verbose_name="объект сети",
                    ),
                ),
            ],
            options={
                "verbose_name": "продукт",
                "verbose_name_plural": "продукты",
            },
        ),
    ]
