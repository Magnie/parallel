from django.conf.urls import url

from . import views
from controllers.topic import ajax as topic_ajax
from controllers.post import ajax as post_ajax

from controllers.tag import views as tag_view
from controllers.topic import views as topic_view

urlpatterns = [
    # Global stuff
    url(r'^$', views.index, name='index'),
    
    # Tag Views and AJAX
    url(r'^tag/(\d+)$', tag_view.tag, name='tag'),
    
    
    # Topic Views and AJAX
    url(r'^ajax/topics/(\d+)$', topic_ajax.get_topics, name='topics'),
    url(r'^topic/(\d+)$', topic_view.topic, name='topic'),
    
    
    # Post Views and AJAX
    url(r'^ajax/posts/(\d+)$', post_ajax.get_posts, name='posts'),
]
