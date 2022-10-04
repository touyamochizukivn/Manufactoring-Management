from django.db import models


PRODUCT_CHOICE = [
    ("Smartphone", "Smartphone"),
    ("Laptop", "Laptop"),
    ("Smartwatch", "Smartwatch"),
]

CONTRACT_STATUS = [
    ("PENDING", "PENDING"),
    ("CONFIRMED", "CONFIRMED"),
    ("DELIVERED", "DELIVERED"),
    ("SETTLEMENTED", "SETTLEMENTED"),
]

class Component(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class PurchaseContract(models.Model):
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=CONTRACT_STATUS, default='PENDING')
    quantily = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.component} - {self.supplier}"

class Stock(models.Model):
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    quantily = models.IntegerField(default=1)
    def __str__(self):
        return f"{self.component} - {self.quantily}"

class Product(models.Model):
    name = models.CharField(max_length=100, choices=PRODUCT_CHOICE)
    def __str__(self):
        return self.name

class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantily = models.IntegerField(default=1)
    def __str__(self):
        return f"{self.product} - {self.quantily}"

class Customer(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.customer}"

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantily = models.IntegerField(default=1)
    status = models.CharField(max_length=100, choices=CONTRACT_STATUS, default='PENDING')
    def __str__(self):
        return f"{self.product} - {self.quantily}"

class Plan(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class SubTask(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Worker(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Machine(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

