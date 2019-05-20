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
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    image = models.ImageField(upload_to='media/servicos', verbose_name='Imagem', null=True, blank=False)

    class Meta:
        ordering = ['title']
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.title

class Publicacoes (models.Model):
    title = models.CharField('Título', max_length=100, null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    image = models.ImageField(upload_to='media/publicacoes', verbose_name='Imagem', null=True, blank=False)
    url = models.URLField('Link', max_length=300,null=True, blank=False)
    
    class Meta:
        ordering = ['-created_date']
        verbose_name = 'Publicação'
        verbose_name_plural = 'Publicações'
    
    def __str__(self):
        return self.title

class Parceiros (models.Model):
    title = models.CharField('Empresa', max_length=100, null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    image = models.ImageField(upload_to='media/parceiros', verbose_name='Imagem', null=True, blank=False)
    url = models.URLField('Link', max_length=300,null=True, blank=False)

    class Meta:
        ordering = ['title']
        verbose_name = 'Parceiro'
        verbose_name_plural = 'Parceiros'
    
    def __str__(self):
        return self.title

class Depoimentos(models.Model):
    nome = models.CharField(max_length = 100, null = False, blank = False, verbose_name = 'Nome')
    imagem = models.ImageField(upload_to = 'media/depoimentos', verbose_name = 'Foto', null = False, blank = False )
    vinculo = models.CharField(max_length = 100, null = False, blank = False, verbose_name = 'Vínculo')
    descricao = models.TextField(verbose_name = 'Descrição', null = False, blank = False)
    created_date = models.DateTimeField(auto_now_add = True, verbose_name = 'Data de Criação')
    class Meta:
        ordering = ['created_date']
        verbose_name = 'Depoimento'
    
    def __str__(self):
        return self.nome