from django.db import models

from users.models import NULLABLE


class NetworkUnit(models.Model):
    TYPE_CHOICES = [
        ('FA', 'Завод'),
        ('RN', 'Розничная сеть'),
        ('IE', 'Индивидуальный предприниматель')
    ]

    LEVEL_CHOICES = [
        ('0', 'Нулевой уровень'),
        ('1', 'Первый уровень'),
        ('2', 'Второй уровень')
    ]

    name = models.CharField(max_length=500, verbose_name='название')
    type = models.CharField(max_length=30, choices=TYPE_CHOICES, verbose_name='тип звена сети')
    level = models.CharField(max_length=15, choices=LEVEL_CHOICES, verbose_name='уровень в иерархии поставок')

    email = models.EmailField(max_length=254, verbose_name='email', **NULLABLE)
    country = models.CharField(max_length=100, verbose_name='страна', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='город', **NULLABLE)
    street = models.CharField(max_length=100, verbose_name='улица', **NULLABLE)
    house_number = models.CharField(max_length=15, verbose_name='номер дома', **NULLABLE)

    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='ссылка на поставщика',
                                 **NULLABLE, related_name='supplied_units')
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                               verbose_name='задолженность перед поставщиком')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='время создания')

    def __str__(self):
        return f'{self.name} - {self.type}'

    class Meta:
        verbose_name = 'объект сети'
        verbose_name_plural = 'объекты сети'


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='название')
    model = models.CharField(max_length=150, verbose_name='модель', **NULLABLE)
    release_date = models.DateField(verbose_name='дата выхода продукта на рынок', **NULLABLE)
    network_unit = models.ForeignKey(NetworkUnit, on_delete=models.CASCADE, verbose_name='объект сети',
                                     related_name='products')

    def __str__(self):
        return f'{self.name}, {self.model}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
