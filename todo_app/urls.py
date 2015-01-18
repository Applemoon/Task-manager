# coding: utf-8
from django.conf.urls import patterns, url
from todo_app import views

urlpatterns = patterns(
    '',
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^add_new_task/$', views.add_new_task, name='add_new_task'),
    url(r'^check_task_done/$', views.check_task_done, name='check_task_done'),
    url(r'^remove_task/$', views.remove_task, name='remove_task'),
)
