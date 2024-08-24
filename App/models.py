from django.db import models

class Menu(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]
    
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, default='M')
    localidade = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nome



