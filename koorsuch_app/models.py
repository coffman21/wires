from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Spec(models.Model):
    MATERIAL_CHOICES = (
        (u'', u'Медь'),
        (u'А', u'Алюминий')
    )
    material = models.CharField(max_length=2, choices=MATERIAL_CHOICES, blank=True)

    INSULATION_CHOICES = (
        (u'В', u'Поливинилхлорид'),
        (u'Пв', u'Сшитый полиэтилен'),
        (u'П', u'Полимерные композиции, не содержащие галогенов')
    )
    insulation = models.CharField(max_length=100, choices=INSULATION_CHOICES, default='E')

    ARMOR_CHOICES = (
        (u'Г', u'Небронированный'),
        (u'Б', u'Броня из стальных оцинкованных лент'),
        (u'Ба', u'Броня из лент алюминия или его сплава'),
        (u'К', u'Броня из круглых стальных оцинкованных проволок'),
        (u'Ка', u'Броня из проволок алюминия или его сплава')
    )
    armor = models.CharField(max_length=100, choices=ARMOR_CHOICES, default='E')

    PROTECTION_CHOICES = (
        (u'В', u'Наружная оболочка из поливинилхлоридного пластиката'),
        (u'Шв', u'Защитный шланг из поливинилхлоридного пластиката'),
        (u'Шп', u'Зашитный шланг из полиэтилена'),
        (u'П', u'Наружная оболочка из полимеров, не содержащих галогенов'),
    )
    protection = models.CharField(max_length=150, choices=PROTECTION_CHOICES, default="E")

    SCREEN_CHOICES = (
        (u'', u'Без экрана'),
        (u'Э', u'С экраном'),
    )
    screening = models.CharField(max_length=100, choices=SCREEN_CHOICES, blank=True)

    non_fire = "Не распространяющие горение при групповой прокладке"
    FIREFIGHTING_CAT_CHOICES = (
        (u'', u'Не распространяющие горение при одиночной прокладке'),
        (u'нг(A F/R)', non_fire + u' по категории A F/R'),
        (u'нг(A)', non_fire + u' по категории A'),
        (u'нг(B)', non_fire + u' по категории B'),
    )
    firefighting_cat = models.CharField(max_length=300, choices=FIREFIGHTING_CAT_CHOICES, blank=True)

    # TODO: make following unavailable when ff_cat is blank

    FIREFIGHTING_SPEC_CHOICES = (
        (u'-LS', u'С пониженным дымо- и газовыделением'),
        (u'-HF', u'Не выделяющие коррозионно-активных '
                 u'газообразных продуктов при горении'),
        (u'-FRLS', u'Огнестойкие, с пониженным дымо- и газовыделением'),
        (u'-FRHF', u'Огнестойкие и не выделяющие коррозионно-активных '
                   u'газообразных продуктов при горении'),
    )
    firefighting_spec = models.CharField(max_length=200, choices=FIREFIGHTING_SPEC_CHOICES, null=True)

    SHAPE_CHOICES = (
        (u'', u'Круглые'),
        (u'П', u'Плоские'),
    )
    shape = models.CharField(max_length=50, choices=SHAPE_CHOICES, default="E")

    IMPLEMENTATION_CHOICES = (
        (u'ок', u'Однопроволочные круглые'),
        (u'мк', u'Многопроволочные круглые'),
        (u'ос', u'Однопроволочные секторные или сегментные'),
        (u'мс', u'Многопроволочные секторные или сегментные'),
    )
    implementation = models.CharField(max_length=100, choices=IMPLEMENTATION_CHOICES, default="E")

    CLIMATE_CHOICES = (
        (u'У', u'Умеренный климат'),
        (u'ХЛ', u'Холодный климат'),
        (u'УХЛ', u'Умеренный и холодный климат'),
        (u'Т', u'Тропический климат'),
        (u'М', u'Морской умеренно-холодный климат'),
        (u'О', u'Общеклиматическое исполнение'),
        (u'ОМ', u'Общеклиматическое морское исполнение'),
        (u'В', u'Всеклиматическое исполнение'),
    )
    climate = models.CharField(max_length=100, choices=CLIMATE_CHOICES, null=True)


class Cable(models.Model):
    name = models.CharField(max_length=100)
    spec = models.ForeignKey(Spec)
    wire = models.IntegerField(default=1, validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
    ])
    extra_wires = models.IntegerField(null=True, default=1, validators=[
        MaxValueValidator(3),
        MinValueValidator(0)
    ])
    GAUGE_CHOICES = (
        (1.5, 1.5),
        (2.5, 2.5),
        (4, 4),
        (6, 6),
        (10, 10),
        (16, 16),
        (25, 25),
        (35, 35),
        (50, 50),
        (70, 70),
        (95, 95),
        (120, 120),
        (150, 150),
        (185, 185),
        (240, 240),
        (300, 300),
        (400, 400),
        (500, 500),
        (625, 625),
        (630, 630),
        (800, 800),
        (1000, 1000)
    )
    gauge = models.FloatField(choices=GAUGE_CHOICES, default=0)

    extra_gauge = models.FloatField(choices=GAUGE_CHOICES, null=True)


