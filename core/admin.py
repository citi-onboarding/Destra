from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import QuemSomos

# # Register your models here.
admin.site.register(QuemSomos, SingletonModelAdmin)
config = QuemSomos.objects.get()