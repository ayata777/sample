from django.conf.urls import include, url
from . import views
app_name = 'app'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ask/(?P<pk>\d+)$', views.ask, name='ask'),
    url(r'^apply$', views.apply, name='apply'),
    url(r'^select/(?P<pk>\d+)$', views.select, name='select'),
    url(r'^good/(?P<pk>\d+)$', views.good, name='good'),
    url(r'^bad/(?P<pk>\d+)$', views.bad, name='bad'),
    url(r'^test$', views.test, name='test'),
]
