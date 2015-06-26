from django.conf.urls import include, url
#from django.conf import settings

from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"), 
	url(r'^/(?P<node_type>(goal|requirement|project))/(?P<node_id>[0-9]+)/$', views.detail, name="detail"),
	url(r'^/(?P<node_type>(goal|requirement|project))/create/$', views.create_node, name="create"),
	url(r'^/(?P<node_type>(goal|requirement|project))/(?P<node_id>[0-9]+)/edit/$', views.edit_node, name="edit"),
	url(r'^/connection/(?P<connection_id>[0-9]+)/$', views.connection_detail, name="connection_detail"),
	url(r'^/connection/(?P<connection_id>[0-9]+)/edit/$', views.edit_connection, name="edit_connection"),
	url(r'^/link/(?P<link_id>[0-9]+)/$', views.link_detail, name="link_detail"),
	url(r'^/link/(?P<link_id>[0-9]+)/edit/$', views.edit_link, name="edit_link"),
#	url(r'^/static/(?P<path>.*)$', django.views.static.serve, {'document_root', settings.STATIC_ROOT})
	]