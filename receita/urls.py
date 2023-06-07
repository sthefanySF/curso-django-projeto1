from django.urls import path
from receita.views import home
from . import views


app_name = 'receitas'

urlpatterns = [
    path('', views.home, name="home"),
    path('receitas/<int:id>/', views.receita, name="receita"),

]