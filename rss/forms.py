# -*- coding: utf-8 -*-

from django.forms import ModelForm
from django import forms
from rss.models import *

class RssForm(ModelForm):
	class Meta:
		model = Lista
