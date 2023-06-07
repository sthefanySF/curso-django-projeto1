from django.shortcuts import render
from django.http import HttpResponse
from Utils.receitas.factory import make_recipe

def home(request):
    return render(request,'receita/pages/home.html', context={
        'receitas' : [make_recipe() for _ in range(10)],
    })

def receita(request, id):
    return render(request,'receita/pages/receita-view.html', context={
        'receita' : make_recipe(),
        'is_datail_page': True,
    })
