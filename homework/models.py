from django.db import models

# Create your models here.

class Product(models.Model):
    """Модель для товаров"""
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=1)

    def set_price(self, price):
        self.price = price

    def set_name(self, name):
        self.name = name


class CustomUser(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    balance = models.DecimalField(decimal_places=1)
    user_type = models.CharField(choices=('staff', 'customer', 'courier'))


customers = CustomUser.objects.filter(user_type='customer')
couriers = CustomUser.objects.filter(user_type='courier')


class Customer(models.Model):
    pass


class Order(models.Model):
    customer = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE())
    price = models.DecimalField(decimal_places=1)
    amount = models.IntegerField()
    status = models.CharField(
        choices=('in progress', 'delivered', 'not delivered'))


class Courier(models.Model):
    name = models.CharField(max_length=100)
    orders = models.ForeignKey(to=Order, on_delete=models.CASCADE())
    ordered_date = models.DateTimeField()


class Staff(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE())

    def new_name(self):
        name = input('Введите новое название: ')
        Product.set_name(name)

    def new_price(self):
        price = float(input('Введите новую цену: '))
        Product.set_price(price)
