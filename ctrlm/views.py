from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from ctrlm.models import Pdl


# Create your views here.


def index(req):
    d = (Pdl.objects.first())
    print(d)
    return render(req, 'index.html', {'elements': Pdl.objects.all()[0:10]})
    # ("Hello world db : {} , les  dix  premieres  valeurs {}".format(Pdl.objects.db, d))


def prm_search(req):
    return render(req, 'pdl.html', {'elements': Pdl.objects.all()[0:10]})


def etab_search(req):
    return render(req, 'pdl.html', {'elements': Pdl.objects.all()[0:10]})


def go(req):
    print('type source: ', len(list(req.FILES)))
    return render(req, 'pdl.html', {'elements': Pdl.objects.all()[0:10]})
    # return HttpResponseRedirect(reverse('ctrlm:pdlquery', args=(Pdl.objects.all()[0:10])))
