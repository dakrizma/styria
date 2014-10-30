from django.shortcuts import render
from django.http import HttpResponseRedirect
from rss.models import *
from rss.forms import *

def index(request):
	if request.method == 'POST':
		form = RssForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	else:
		form = RssForm()
	return render(request, 'rss/index.html', {'form': form})
