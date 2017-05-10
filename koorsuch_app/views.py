from django.shortcuts import render
from django.forms import ModelForm
from django.views import View

from .models import Spec, Cable
from .form import CableForm

class CableFormView(View):
    form_class = CableForm
    initial = {'key': 'value'}
    class Meta:
        model = Spec
        fields = ('material', 'insulation', 'armor', 'protection', 'screening',
                  'firefighting_cat', 'firefighting_spec', 'shape', 'implementation',
                  'climate')

    def get(self, request, *args, **kwargs):
        # dunno wat is this
        form = self.form_class(initial=self.initial)
        return render(request, 'koorsuch/index.html', {'form': form})

def index(request):
    specs = Spec.objects.all()
    cables = Cable.objects.all()



    context = {
        'cables': cables,
        'specs':  specs
    }

    return render(request, 'koorsuch/index.html', context)
