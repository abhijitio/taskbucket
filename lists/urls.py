from django.conf.urls import url

from lists import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^todolist/(?P<todolist_id>\d+)/$', views.todolist, name='todolist'),
    url(r'^todolist/new/$', views.new_todolist, name='new_todolist'),
    url(r'^todolist/add/$', views.add_todolist, name='add_todolist'),
    url(r'^todo/add/(?P<todolist_id>\d+)/$', views.add_todo, name='add_todo'),
    url(r'^todolists/$', views.overview, name='overview'),
    url(r'^(?P<todo_id>[0-9]+)/$', views.delete_task, name='delete_task'),
    url(r'^catdel/(?P<cat_id>[0-9]+)/$', views.cat_del, name='cat_del')
    
        
]
