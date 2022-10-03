from django.shortcuts import render
from . import models

# Create your views here.
def index (request):
    allpelayanobj = models.pelayan.objects.all()
    getpelayanobj = models.pelayan.objects.get(idpelayan='P01')

    return render(request, 'pelayan.html',{
        "allpelayanobj" : allpelayanobj,
        "getpelayanobj" : getpelayanobj,
    })

def createdata(request):
    if request.method == 'GET':
        return render(request, 'createdata.html')
    else :
        namapelayan = request.POST['namapelayan']
        notelp = request.POST['notelp']
        alamat = request.POST['alamat']


        newpelayan = models.pelayan(
            namapelayan = namapelayan,
            notelp = notelp,
            alamat = alamat
        )
        newpelayan.save()
        return ('index')
