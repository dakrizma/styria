from django.conf.urls import patterns, url
from rss import views

urlpatterns = patterns('',
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^unos/$', views.RssView.as_view(), name='unos'),
)