from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from ping.models import Raspberry


def test(request):

    raspb = Raspberry.objects.all()

    t = loader.get_template('ping/test.html')
    c = Context({
        'raspb': raspb,
    })
    return HttpResponse(t.render(c))

def ajax_cadence(request):
    for rasp in Raspberry.objects.all():
        cadence = str(rasp.cadence)
    return HttpResponse(cadence)

def ajax_vitesse(request):
    for rasp in Raspberry.objects.all():
        vitesse = str(rasp.vitesse)
    return HttpResponse(vitesse)