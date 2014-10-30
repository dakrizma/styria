from django.contrib import admin
from rss.models import *

class ListaAdmin(admin.ModelAdmin):
	list_display = ('title', 'link')
	list_filter = ('status',)

admin.site.register(Lista, ListaAdmin)