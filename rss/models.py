from django.db import models


class Lista(models.Model):
	title = models.CharField(max_length=200)
	link = models.CharField(max_length=200)
	status = models.BooleanField("RSS feed aktivan?", default = True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name_plural = 'liste'