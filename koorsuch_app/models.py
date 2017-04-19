from django.db import models


class Spec(models.Model):
    MATERIAL_CHOICES = (
        (u'_', u'Медь'),
        (u'А', u'Алюминий')
    )
    material = models.CharField(max_length=2, choices=MATERIAL_CHOICES)

    INSULATION_CHOICES = (
        (u'В', u'Поливинилхлорид'),
        (u'Пв', u'Сшитый полиэтилен'),
        (u'П', u'Полимерные композиции, не содержащие галогенов')
    )
    insulation = models.CharField(max_length=100, choices=INSULATION_CHOICES)



class Cable(models.Model):
    name = models.CharField(max_length=100)
    spec = models.ForeignKey(Spec)




    # TODO: create fields:
    # - armor
    # - protection
    # - screen
    # - implementation
    # - climate
