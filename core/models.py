from django.db import models


class Smartphone(models.Model):
    class Meta:
        verbose_name = 'Smartphone'
        verbose_name_plural = 'Smmartphones'

    name = models.CharField(_(""), max_length=100),
    model = models.CharField(_(""), max_length=100),
    imei = models.CharField(_(""), max_length=100),
    serial_number = models.CharField(_(""), max_length=100),
    color = models.CharField(_(""), max_length=100),
    image = models.CharField(_(""), max_length=100),
    mfg = models.CharField(_(""), max_length=100),
    release_date = models.CharField(_(""), max_length=100),
    specification = models.CharField(_(""), max_length=100),
    description = models.CharField(_(""), max_length=100),
    price = models.CharField(_(""), max_length=100),

    def __str__(self):
        return self.name
    