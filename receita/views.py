from django.shortcuts import render
from django.http import HttpResponse
from Utils.receitas.factory import make_recipe
from receita.models import Recipe

def home(request):
    receita = Recipe.objects.filter(
        is_published=True #fazer com que as receitas que não foram publicadas não apareçam
    ).order_by('-id') #buscar todas as receitas e ordena-las
    return render(request,'receita/pages/home.html', context={
        'receitas' : receita,
    })

def category(request, category_id):
    receita = Recipe.objects.filter(
        category__id=category_id,
        is_published=True).order_by('-id') 
    return render(request,'receita/pages/home.html', context={
        'receitas' : receita,
    })


def receita(request, id):
    return render(request,'receita/pages/receita-view.html', context={
        'receita' : make_recipe(),
        'is_datail_page': True,
    })
