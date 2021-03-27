from django.db import models
from django.core.exceptions import ValidationError

from ares_util.ares import call_ares


def validate_ares(value):
    ares = call_ares(value)

    if not ares:
        raise ValidationError(f"{value} is not a valid ares")


class Company(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True, max_length=255)
    ico = models.CharField(max_length=8, validators=[validate_ares])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "companies"
