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
    class Meta:
        verbose_name_plural = '1. Components'
        verbose_name = 'Component'
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Supplier(models.Model):
    class Meta:
        verbose_name_plural = '1.1 Suppliers'
        verbose_name = 'Supplier'
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class PurchaseOrder(models.Model):
    class Meta:
        verbose_name_plural = '1.3 PurchaseOrder'
        verbose_name = 'PurchaseOrder'
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.supplier}"

class PurchaseOrderDetail(models.Model):
    class Meta:
        verbose_name_plural = '1.3.1 PurchaseOrderDetail'
        verbose_name = 'PurchaseOrderDetail'
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=CONTRACT_STATUS, default='PENDING')
    quantily = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.component} - {self.quantily}"

class Stock(models.Model):
    class Meta:
        verbose_name_plural = '1.2 Stock'
        verbose_name = 'Stock'
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    quantily = models.IntegerField(default=1)
    def __str__(self):
        return f"{self.component} - {self.quantily}"

class Product(models.Model):
    class Meta:
        verbose_name_plural = '2. Products'
        verbose_name = 'Product'
    name = models.CharField(max_length=100, choices=PRODUCT_CHOICE)
    component = models.ManyToManyField(Component, related_name="Assembly")
    def __str__(self):
        return self.name

class Customer(models.Model):
    class Meta:
        verbose_name_plural = '2.1 Customers'
        verbose_name = 'Customer'
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Inventory(models.Model):
    class Meta:
        verbose_name_plural = '2.2 Inventory'
        verbose_name = 'Inventory'
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantily = models.IntegerField(default=1)
    def __str__(self):
        return f"{self.product} - {self.quantily}"

class SaleOrder(models.Model):
    class Meta:
        verbose_name_plural = '2.3 SaleOrder'
        verbose_name = 'SaleOrder'
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.customer}"

class SaleOrderDetail(models.Model):
    class Meta:
        verbose_name_plural = '2.3.1 SaleOrderDetail'
        verbose_name = 'SaleOrderDetail'
    order = models.ForeignKey(SaleOrder, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantily = models.IntegerField(default=1)
    status = models.CharField(max_length=100, choices=CONTRACT_STATUS, default='PENDING')
    def __str__(self):
        return f"{self.product} - {self.quantily}"

class Plan(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    responsible = models.ForeignKey(SaleOrder, on_delete=models.CASCADE)
    week_number = models.CharField(max_length=2, blank=True)
    end_date = models.DateField()

    def __str__(self):
        return str(self.name)
    
    def save(self, *args, **kargs):
        print(self.start_date.isocalendar()[1])
        if self.week_number == "":
            self.week_number = self.start_date.isocalendar()[1]
        super().save(*args, **kargs)

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

