from django.db import models


class Lista(models.Model):
	title = models.CharField(max_length=200)
	link = models.CharField(max_length=200)
	# status = models.CharField(max_length=1, choices=((True, 'Da'),(False, 'Ne')), null=False)
	status = models.BooleanField("RSS feed aktivan?")

	def __str__(self):
		return self.title

	class Meta:
		verbose_name_plural = 'liste'