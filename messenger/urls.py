from django.conf.urls import url

from . import views

app_name = 'messenger'

urlpatterns = [
    url(r'^$', views.messageListView.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)/$', views.messageDetailView.as_view(), name='detail'),
]
