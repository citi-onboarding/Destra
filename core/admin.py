from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import QuemSomos
from .models import Servicos
from .models import Publicacoes

admin.site.register(QuemSomos, SingletonModelAdmin)
config = QuemSomos.objects.get()

class ServicosAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date')

class PublicacoesAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date')

admin.site.register(Servicos, ServicosAdmin)
admin.site.register(Publicacoes)
