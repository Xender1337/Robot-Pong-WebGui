from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response, get_object_or_404

from ping.models import Raspberry


def test(request):

    raspb = Raspberry.objects.all()

    t = loader.get_template('ping/test.html')
    c = Context({
        'raspb': raspb,
    })
    return HttpResponse(t.render(c))