from django.db import models
from django.utils.translation import gettext_lazy as _


class Smartphone(models.Model):
    class Meta:
        verbose_name = 'Smart Phone'
        verbose_name_plural = 'Smart Phones'

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
    