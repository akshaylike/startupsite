from django.conf.urls import patterns, include, url
from startups import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    #url(r'^upvote/$', views.upvote, name='upvote'),
    #url(r'^downvote/$', views.downvote, name='downvote'),
    url(r'^add_comment/$', views.add_comment, name='add_comment'),
    url(r'^vote/$', views.vote, name='vote'),
)
