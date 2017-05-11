from django.db import models
from django.forms import ModelForm
from django.core.validators import MaxValueValidator, MinValueValidator

from .choices import *
# default="E" means that current value should've been selected from the list but not missed
class Spec(models.Model):

    material = models.CharField(max_length=2, choices=MATERIAL_CHOICES, blank=True)
    insulation = models.CharField(max_length=100, choices=INSULATION_CHOICES, default='E')
    armor = models.CharField(max_length=100, choices=ARMOR_CHOICES, default='E')
    protection = models.CharField(max_length=150, choices=PROTECTION_CHOICES, default="E")
    screening = models.CharField(max_length=100, choices=SCREEN_CHOICES, blank=True)
    firefighting_cat = models.CharField(max_length=300, choices=FIREFIGHTING_CAT_CHOICES, blank=True)

    # TODO: make following unavailable when ff_cat is blank

    firefighting_spec = models.CharField(max_length=200, choices=FIREFIGHTING_SPEC_CHOICES, null=True, blank=True)
    shape = models.CharField(max_length=50, choices=SHAPE_CHOICES, default="E", blank=True)
    implementation = models.CharField(max_length=100, choices=IMPLEMENTATION_CHOICES, default="E")
    climate = models.CharField(max_length=100, choices=CLIMATE_CHOICES, null=True)

    def __str__(self):
        return self.material + self.insulation + self.protection + self.armor + self.screening


class Cable(models.Model):
    name = models.CharField(max_length=100)
    spec = models.ForeignKey(Spec)
    wire = models.IntegerField(default=2, validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
    ])
    extra_wires = models.IntegerField(blank=True, null=True, default=0, validators=[
        MaxValueValidator(3),
        MinValueValidator(0)
    ])
    gauge = models.FloatField(choices=GAUGE_CHOICES, default=0)

    extra_gauge = models.FloatField(choices=GAUGE_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.name

