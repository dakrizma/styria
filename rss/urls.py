from django.conf.urls import patterns, url
from rss import views

urlpatterns = patterns('',
	url(r'^$', views.RssView.as_view(), name='index'),
	url(r'^(?P<pk>\d+)/$', views.RssUpdateView.as_view(), name='update'),
	# url(r'^temp', views.WordView.as_view(), name='word'),
	url(r'^temp', views.Print.as_view(), name='word'),
)