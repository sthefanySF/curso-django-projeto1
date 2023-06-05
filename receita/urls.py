from django.urls import path
from receita.views import home
from . import views




urlpatterns = [
    path('', home),
    path('', views.home),
    path('receitas/<int:id>/', views.receita), #esse int antes do ir é para só ser permitido passar numero na url

]