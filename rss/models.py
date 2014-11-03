from django.db import models

class Feed(models.Model):
	link = models.URLField()
	status = models.BooleanField("RSS feed aktivan?", default = True)

	def __unicode__(self):
		return self.link

class Entry(models.Model):
	title = models.CharField(max_length=300)
	url = models.URLField()
	description = models.TextField()
	feed = models.ForeignKey(Feed)

	def __unicode__(self):
		return self.title

class Word(models.Model):
	word = models.CharField(max_length=50)
	
	def __unicode__(self):
		return self.word

class WordCount(models.Model):
	word = models.ForeignKey(Word)
	entry = models.ForeignKey(Entry)
	sum_entry = models.IntegerField(default=0)
	feed = models.ForeignKey(Feed)
	sum_feed = models.IntegerField(default=0)
	total = models.IntegerField(default=0)

	def __unicode__(self):
		return self.word