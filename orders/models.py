from django.db import models
from shop.models import Product
from django.core.validators import RegexValidator

DELIVERY_CHOICES = (
    ('Новая почта', 'Новая почта'),
    ('Деливери', 'Деливери'),
    ('Укрпочта', 'Укрпочта'),
    ('Интайм', 'Интайм'),
    ('Самовывоз', 'Самовывоз'),
    ('', 'Не указано'),
)

class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250, blank=True, default='')
    postal_code = models.CharField(verbose_name='Почтовый индекс', max_length=20, blank=True, default='')
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    text = models.TextField("Дополнительная информция", blank=True, default='')
    paid = models.BooleanField(verbose_name='Оплата', default=False)
    sent = models.BooleanField(verbose_name='Отправленно', default=False)
    delivery = models.CharField(max_length=50, choices=DELIVERY_CHOICES, blank=True, default='')
    phone_regex = RegexValidator(regex=r'^\d{10,15}$',
        message="Введите украинский телефонный номер в формате код оператора + номер телефона: '0671234567'. От 10 до 15 цифр."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=15, default='')


    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity


"""
from django.db import models
from shop.models import Product


class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
"""
