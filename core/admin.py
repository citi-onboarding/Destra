from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import QuemSomos
from .models import Servicos
from .models import Publicacoes
from .models import Parceiros

class ServicosAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date')

class PublicacoesAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date')

class ParceirosAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date')

admin.site.register(Servicos, ServicosAdmin)
admin.site.register(Publicacoes, PublicacoesAdmin)
admin.site.register(QuemSomos, SingletonModelAdmin)
admin.site.register(Parceiros, ParceirosAdmin)

if(len(QuemSomos.objects.all())>0):
    config = QuemSomos.objects.get()
