from django.db import models
from solo.models import SingletonModel

# Create your models here.
class QuemSomos(SingletonModel):
    descricao = models.TextField()
    missao = models.TextField()
    visao = models.TextField()
    valores = models.TextField()
    
    def __str__(self):
        return "Quem somos"

    class Meta:
        verbose_name = "Quem somos"

