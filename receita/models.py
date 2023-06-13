from django.db import models
from django.contrib.auth.models import User #usuario do django/tabela da base de dados


class Category(models.Model): #tabela de categoria de receitas
    name = models.CharField(max_length=65)

    def __str__(self): #metodo magico para salvar o nome da categonia de acordo com o que foi escrito 
        return self.name


class Recipe(models.Model): #tabela de receitas
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='receita/covers/%Y/%m/%d/')
    #relação de tabelas

    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    

    def __str__(self):
        return self.title #para que o titulo da receita que a gente colocou apareça

    