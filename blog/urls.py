from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'), #an empty URL will redirect to the view 'post_list'
]