from django.contrib import admin
from rss.models import *

class FeedAdmin(admin.ModelAdmin):
	list_display = ('id', 'link')
	list_filter = ('status',)

class EntryAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'url', 'description', 'feed')

class WordAdmin(admin.ModelAdmin):
	list_display = ('word',)

class WordCountAdmin(admin.ModelAdmin):
	list_display = ('sum_entry', 'total')

admin.site.register(Feed, FeedAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Word, WordAdmin)
admin.site.register(WordCount, WordCountAdmin)