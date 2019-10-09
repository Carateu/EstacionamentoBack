from django.contrib import admin
from .models import (
    Pessoa,
    Marca,
    Veiculo,
    Parametros,
    MovRotativo,
    Mensalista,
    MovMensalista,
    )



class MovimentoRotativoAdmin(admin.ModelAdmin):
    list_display = ('checkin','checkout','valor_hora','veiculo','pago','horas_total','total')

class MovimentoMensalAdmin(admin.ModelAdmin):
    list_display = ('mensalista','data_pgto','total')


admin.site.register(Pessoa)
admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Parametros)
admin.site.register(MovRotativo, MovimentoRotativoAdmin)
admin.site.register(Mensalista)
admin.site.register(MovMensalista, MovimentoMensalAdmin)

