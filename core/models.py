from django.db import models
from django.utils.translation import gettext_lazy as _


class Smartphone(models.Model):
    class Meta:
        verbose_name = 'Smartphone'
        verbose_name_plural = 'Smartphones'

    name = models.CharField(_("name"), max_length=100),
    model = models.CharField(_("model"), max_length=100),
    imei = models.CharField(_("imei"), max_length=100),
    serial_number = models.CharField(_("serial_number"), max_length=100),
    color = models.CharField(_("color"), max_length=100),
    image = models.CharField(_("image"), max_length=100),
    mfg = models.CharField(_("mfg"), max_length=100),
    release_date = models.CharField(_("release_date"), max_length=100),
    specification = models.CharField(_("specification"), max_length=100),
    description = models.CharField(_("description"), max_length=100),
    price = models.CharField(_("price"), max_length=100),

    def __str__(self):
        return self.name
    

class Component(models.Model):
    class Meta:
        verbose_name = 'Component'
        verbose_name_plural = 'Components'
    
    name = models.CharField(_("name"), max_length=100)

    def __str__(self):
        return self.name

class MSmartphone(models.Model):
    class Meta:
        verbose_name = 'MSmartphone'
        verbose_name_plural = 'MSmartphones'
    
    smartphone = models.ForeignKey(Smartphone, verbose_name=_("smartphone"), on_delete=models.CASCADE)
    component = models.ForeignKey(Component, verbose_name=_("component"), on_delete=models.CASCADE)

    def __str__(self):
        return self.smartphone

class Customer(models.Model):
    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
    
    name = models.CharField(_("name"), max_length=100)

    def __str__(self):
        return self.name

class Partners(models.Model):
    class Meta:
        verbose_name = 'Partners'
        verbose_name_plural = 'Partners'
    
    name = models.CharField(_("name"), max_length=100)

    def __str__(self):
        return self.name

class Contract(models.Model):
    class Meta:
        verbose_name = 'Contract'   
        verbose_name_plural = 'Contracts'
    
    name = models.CharField(_("name"), max_length=100)

    def __str__(self):
        return self.name

class Plan(models.Model):
    class Meta:
        verbose_name = 'Plan'
        verbose_name_plural = 'Plans'
    
    name = models.CharField(_("name"), max_length=100)

    def __str__(self):
        return self.name
    