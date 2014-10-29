# -*- coding: utf-8 -*-
from django.db import models


class Lista(models.Model):
	status_choice = (
		('d', 'Da'),
		('n', 'Ne'),
		)
	title = models.CharField(max_length=200)
	link = models.CharField(max_length=200)
	status = models.CharField(max_length=1, choices=status_choice)
		