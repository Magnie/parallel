from django.conf.urls import url

from . import views
from controllers.topic import ajax as topic_ajax
from controllers.post import ajax as post_ajax

from controllers.tag import views as tag_view
from controllers.topic import views as topic_view

from controllers.auth import ajax as auth_ajax
from controllers.nav import ajax as nav_ajax

urlpatterns = [
    # Global stuff
    url(r'^$', views.index, name='index'),
    
    # Tag Views and AJAX
    url(r'^tag/(\d+)$', tag_view.tag, name='tag'),
    
    
    # Topic Views and AJAX
    url(r'^ajax/topics/(\d+)$', topic_ajax.get_topics, name='topics'),
    url(r'^ajax/topics/create$', topic_ajax.create_topic, name='new_topic'),
    url(r'^topic/(\d+)$', topic_view.topic, name='topic'),
    
    
    # Post Views and AJAX
    url(r'^ajax/posts/(\d+)$', post_ajax.get_posts, name='posts'),
    url(r'^ajax/posts/create_post$', post_ajax.create_post, name='new_post'),
    
    # Authentication AJAX
    url(r'^ajax/auth/logout', auth_ajax.logout_ajax, name='logout'),
    url(r'^ajax/auth/login', auth_ajax.login, name='login'),
    url(r'^ajax/auth/register', auth_ajax.register, name='register'),
    
    # Navigation
    url(r'^ajax/nav/menu', nav_ajax.get_nav, name='nav_menu'),
]
