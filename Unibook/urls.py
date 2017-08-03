from django.conf.urls import url
from . import views
app_name = 'Unibook'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^donation$', views.donation, name='donation'),
	url(r'^index$', views.index, name='index')
]