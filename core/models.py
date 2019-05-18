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

class Servicos (models.Model):
    title = models.CharField('Título', max_length=100, null=False, blank=False)
    text = models.TextField('Descrição', null=True, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media/servicos', verbose_name='Imagem', null=True, blank=False)

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.title

class Publicacoes (models.Model):
    title = models.CharField('Título', max_length=100, null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    url = models.URLField('Link', max_length=300,null=True, blank=False)
    image = models.ImageField(upload_to='media/publicacoes', verbose_name='Imagem', null=True, blank=False)
    
    # url = models.URLField(max_length=300)

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'Publicação'
        verbose_name_plural = 'Publicações'
    
    def __str__(self):
        return self.title
