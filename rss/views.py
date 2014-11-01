from django.views.generic import FormView, ListView, View

from rss.models import *
from rss.forms import *

class RssView(FormView):
	template_name = 'rss/index.html'
	form_class = RssForm
	success_url = '/'

	def form_valid(self, form):
		form.save()
		return super(RssView, self).form_valid(form)
	
	# def get_queryset(self):
	# 	return Lista.objects.order_by('-pk')

class IndexView(ListView):
	template_name = 'rss/index.html'

	def get_queryset(self):
		return Lista.objects.order_by('-pk')

class IndexSView(View):

	def get(self, request, *args, **kwargs):
		view = IndexView.as_view()
		return view(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		view = RssView.as_view()
		return view(request, *args, **kwargs)
