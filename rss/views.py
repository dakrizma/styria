from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic.edit import FormView, FormMixin
from django.views.generic.list import ListView

from rss.models import *
from rss.forms import *

# def unos(request):
# 	if request.method == 'POST':
# 		form = RssForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			return HttpResponseRedirect('/')
# 	else:
# 		form = RssForm()
# 	return render(request, 'rss/index.html', {'form': form})

# class IndexView(generic.ListView):
# 	model = Lista
# 	template_name = 'rss/index.html'

class RssView(FormView):
	template_name = 'rss/index.html'
	form_class = RssForm
	success_url = '/'

	def form_valid(self, form):
		form.save()
		return super(RssView, self).form_valid(form)

class IndexView(ListView, FormMixin):
	model = Lista
	template_name = 'rss/index.html'
	form_class = RssForm
	success_url = '/'

	def form_valid(self, form):
		form.save()
		return super(IndexView, self).form_valid(form)
