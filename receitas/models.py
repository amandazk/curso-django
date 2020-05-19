from django.db import models
from datetime import datetime

# Create your models here.
class Receita(models.Model):
    nome_receita = models.CharField(max_length = 200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.TextField(max_length = 100)
    categoria = models.CharField(max_length = 100)
    data_receita = models.DateTimeField(default = datetime.now, blank = True)
    def __str__(self): #pra mostrar o nome no bd
        return self.nome_receita

