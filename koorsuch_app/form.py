from django import forms
from django.forms import ModelForm

from .models import Cable, Spec
from .choices import *


# following should be redundant
"""
class SpecForm(forms.Form):
    material = forms.ChoiceField(choices=MATERIAL_CHOICES, label='материалоо', initial='', required=True)
    insulation = forms.ChoiceField(choices=INSULATION_CHOICES, label='', initial='', required=True)
    armor = forms.ChoiceField(choices=ARMOR_CHOICES, label='', initial='', required=True)
    protection = forms.ChoiceField(choices=PROTECTION_CHOICES, label='', initial='', required=True)
    screening = forms.ChoiceField(choices=SCREEN_CHOICES, label='', initial='', required=True)
    firefighting_cat = forms.ChoiceField(choices=FIREFIGHTING_CAT_CHOICES, label='', initial='', required=True)

    # TODO: make following unavailable when ff_cat is blank
    firefighting_spec = forms.ChoiceField(choices=FIREFIGHTING_SPEC_CHOICES, label='', initial='')

    shape = forms.ChoiceField(choices=SHAPE_CHOICES, label='', initial='', required=True)
    implementation = forms.ChoiceField(choices=IMPLEMENTATION_CHOICES, label='', initial='', required=True)
    climate = forms.ChoiceField(choices=CLIMATE_CHOICES, label='', initial='')

    class Meta:
        model = Spec


class CableForm(forms.Form):
    name = forms.CharField(label='Название', max_length=100)
    # TODO: select spec here somehow
    wire = forms.ChoiceField(choices=WIRE_CHOICES, initial=2, required=True)
    extra_wires = forms.ChoiceField(choices=EXTRA_WIRE_CHOICES, initial=0)
    # TODO: select gauge by scroll but not by ChoiceField
    gauge = forms.ChoiceField(choices=GAUGE_CHOICES, required=True)
    extra_gauge = forms.ChoiceField(choices=GAUGE_CHOICES)

    def build_name(self):
        # TODO: to build name from spec
        pass

    class Meta:
        model = Cable

"""


class CableForm(ModelForm):
    class Meta:
        model = Cable
        fields = "__all__"


class SpecForm(ModelForm):
    class Meta:
        model = Spec
        fields = '__all__'
