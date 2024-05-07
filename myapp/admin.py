from django.contrib import admin
from myapp import models
from .models import Imovel, ImovelImagem

# Register your models here.
admin.site.register(models.Cliente)
admin.site.register(models.Registro)
admin.site.register(models.Subscriber)
admin.site.register(models.Sobre)

#admin.site.register(models.Imovel)
#admin.site.register(models.ImovelImagem)

class ImovelImagemInlineAdmin(admin.TabularInline):
    model = ImovelImagem
    extra = 0
    
class ImovelAdmin(admin.ModelAdmin):
    inlines = [ImovelImagemInlineAdmin]
    
admin.site.register(models.Imovel, ImovelAdmin)
