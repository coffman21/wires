from django.shortcuts import render
from django.views import View

from .models import Spec, Cable
from .form import CableForm


class CableFormView(View):
    form_class = CableForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        # dunno wat is this
        form = self.form_class()
        return render(request, 'koorsuch/index.html', {'form': form})


def index(request):
    cables = Cable.objects.all()
    # говнокод во все поля
    if 'nm' in request.GET:
        cables = cables.filter(name__contains=request.GET['nm'])
    if 'mt' in request.GET and request.GET['mt'] != '~':
        cables = cables.filter(spec__material=request.GET['mt'])
    if 'is' in request.GET and request.GET['is'] != '':
        cables = cables.filter(spec__insulation=request.GET['is'])
    if 'ar' in request.GET and request.GET['ar'] != '':
        cables = cables.filter(spec__armor=request.GET['ar'])
    if 'pr' in request.GET and request.GET['pr'] != '':
        cables = cables.filter(spec__protection=request.GET['pr'])
    if 'sc' in request.GET and request.GET['sc'] != '~':
        cables = cables.filter(spec__screening=request.GET['sc'])
    if 'ff' in request.GET and request.GET['ff'] != '~':
        cables = cables.filter(spec__firefighting_cat=request.GET['ff'])
    if 'im' in request.GET and request.GET['im'] != '':
        cables = cables.filter(spec__implementation=request.GET['im'])
    if 'sh' in request.GET and request.GET['sh'] != '':
        cables = cables.filter(spec__shape=request.GET['sh'])
    if 'cl' in request.GET and request.GET['cl'] != '':
        cables = cables.filter(spec__climate=request.GET['cl'])
    if 'wr' in request.GET and request.GET['wr'] != '':
        cables = cables.filter(wire=request.GET['wr'])
    if 'xwr' in request.GET and request.GET['xwr'] != '':
        cables = cables.filter(extra_wires=request.GET['xwr'])
    if 'ga' in request.GET and request.GET['ga'] != '':
        cables = cables.filter(gauge__lte=request.GET['ga'])
    if 'xga' in request.GET and request.GET['xga'] != '':
        cables = cables.filter(extra_gauge__lte=request.GET['xga'])

    context = {
        'cables': cables,
    }

    return render(request, 'koorsuch/index.html', context)
