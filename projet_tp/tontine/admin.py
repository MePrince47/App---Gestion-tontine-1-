from django.contrib import admin
from .models import La_tontine
from .models import Le_membre
# Register your models here.

@admin.register(La_tontine)
class La_tontineAdmin(admin.ModelAdmin):
	list_display = ('id','nom','slogan','regle')
@admin.register(Le_membre)
class La_tontineAdmin(admin.ModelAdmin):
	list_display = ('id','nom','Prénom','Email','tontine','Nombre_parts','statut')
