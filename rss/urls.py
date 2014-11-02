from django.conf.urls import patterns, url
from rss import views

urlpatterns = patterns('',
	url(r'^$', views.RssView.as_view(), name='index'),
	url(r'^(?P<pk>\d+)/$', views.RssUpdateView.as_view(), name='update'),
)