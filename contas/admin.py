from django.contrib import admin
from contas.models import Cliente , Filme, Locacao

admin.site.register(Cliente)
admin.site.register(Filme)
admin.site.register(Locacao)