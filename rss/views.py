from django.views.generic import ListView, View
from django.views.generic.edit import FormMixin, UpdateView
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render
import feedparser

from rss.models import *
from rss.forms import *


class RssFormMixin(FormMixin):
	'''
		Feed forma
	'''
	form_class = RssForm
	success_url = '/'

	def form_valid(self, form):
		form.save()
		return super(RssFormMixin, self).form_valid(form)

	def form_invalid(self, form):
		return super(RssFormMixin, self).form_valid(form)

	def post(self, form):
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)

class RssView(RssFormMixin, ListView):
	'''
		Feed forma & Feed lista
	'''
	template_name = "rss/index.html"
	model = Feed
	paginate_by = 10

	def get_queryset(self):
		return Feed.objects.order_by('-pk')

	def get(self, *args, **kwargs):
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		self.object_list = self.get_queryset()
		allow_empty = self.get_allow_empty()
		if not allow_empty and len(self.object_list) == 0:
			raise Http404(_(u"Empty list and '%(class_name)s.allow_empty' is False.") % {'class_name': self.__class__.__name__})
		context = self.get_context_data(object_list=self.object_list, form=form, **kwargs)
		return self.render_to_response(context)

class RssUpdateView(UpdateView):
	'''
		Feed (status) editiranje
	'''
	template_name = "rss/update.html"
	model = Feed

	def get_success_url(self):
		return reverse('rss:index')

	def get_context_data(self, **kwargs):
		context = super(RssUpdateView, self).get_context_data(**kwargs)
		context['action'] = reverse('rss:update', kwargs={'pk': self.get_object().pk})
		return context

class Words():

	def word_count():
		feed = feedparser.parse('https://sg.entertainment.yahoo.com/rss/')
		for i in range(0, len(feed['entries'])):
			p = Entry.objects.create(
				title = feed['entries'][i].title,
				description = feed['entries'][i].description,
				url = feed['entries'][i].link,
				feed = Feed.objects.get(id=1)
			)
			p.save
	
		# context = {'title': title, 'description': description, 'url': url,}
		# return render(request, 'rss/temp.html', context)
	
# 	def remove_tags(description):
# 		result = 0
# 		return result

class WordView(ListView):
	
	def word_count():
		feed = feedparser.parse('https://sg.entertainment.yahoo.com/rss/')
		for i in range(0, len(feed['entries'])):
			p = Entry.objects.create(
				title = feed['entries'][i].title,
				description = feed['entries'][i].description,
				url = feed['entries'][i].link,
				feed = Feed.objects.get(id=1)
			)
			p.save()

	word_count()
	template_name = "rss/temp.html"
	model = Entry
	paginate_by = 10

	def get_queryset(self):
		return Entry.objects.all()

# class Iz(object):
# 	def novi(self):
# 		data = 3
# 		return data

# class Print(Iz, View):
# 	def izlaz(request):
# 		context = 3
# 		# Super(Iz, self).novi()
# 		return render(request, 'rss/temp.html', {'data': context})
# 	izlaz(self)