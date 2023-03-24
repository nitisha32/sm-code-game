from django.conf.urls import url

from . import views

app_name = 'codinggamev1'

urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^choose_theme/$', views.choose_theme, name='choose_theme'),
    url(r'^tutorial/$', views.tutorial, name='tutorial'),
    url(r'^exercises/$', views.exercises, name='exercises'),
]