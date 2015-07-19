# AJAX for posts
"""
Model Reference
-----
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    parent = models.ForeignKey('Post', blank=True)
    text = models.TextField()
    author = models.ForeignKey(User, blank=True)
    post_date = models.DateTimeField()
    
    class Meta:
        ordering = ['post_date']
-----
"""

from django.utils import timezone
from django.http import JsonResponse
from forum.models import Tag, Topic, Post, TopicPost
from forum.utils import *

def get_posts(request, topic_id, offset='0'):
    """
    desc: Get a list of posts
    params: int topic_id, int offset
    return: array({int post_id, str post_author, int author_id, post_text, post_date}) posts
    """
    response = {
        'success': False,
        'posts': [],
        'pages': 0,
    }
    offset = int(offset)
    # Validate input
    if topic_id:
        topic = Topic.objects.get(pk=topic_id)
        
        # If valid, execute.
        if topic:
            start = POSTS_PER_PAGE * offset
            end = start + POSTS_PER_PAGE
            temp_posts = topic.posts.all()
            posts_count = temp_posts.count()
            pages = (posts_count + POSTS_PER_PAGE - 1) / POSTS_PER_PAGE
            temp_posts = temp_posts[start:end]
            posts = []
            for p in temp_posts:
                name = '{0} {1}'.format(p.author.first_name, p.author.last_name)
                if name == ' ':
                    name = p.author.username
                posts.append({
                    'parent_id': p.parent.id if p.parent else 0,
                    'post_id': p.id,
                    'post_author': name,
                    'author_id': p.author.id,
                    'post_text': p.text,
                    'post_date': p.post_date.strftime('%a, %d %b %Y %H:%M:%S')
                })
            
            # Set the response
            response['posts'] = posts
            response['pages'] = pages
            
            # Everything was successful!
            response['success'] = True

    # Return results
    return JsonResponse(response)

def get_micro(request, post_id):
    """
    desc: Get a list of posts and it's replies
    params: int post_id
    return: array({int post_id, str author_name, int author_id, text, date}) posts
    """
    response = {
        'success': False,
        'posts': []
    }

    # Validate input
    if post_id:
        post = Topic.objects.filter(id=post_id)
        
        # If valid, execute.
        if topic:
            temp_posts = topic.posts.all()
            posts = []
            for p in temp_posts:
                posts.append({
                    'parent_id': p.parent.id if p.parent else 0,
                    'post_id': p.id,
                    'post_author': p.author.username,
                    'author_id': p.author.id,
                    'post_text': p.text,
                    'post_date': p.post_date.strftime('%a, %d %b %Y %H:%M:%S')
                })
            
            # Set the response
            response['posts'] = posts
            
            # Everything was successful!
            response['success'] = True

    # Return results
    return JsonResponse(response)

def create_post(request):
    """
    desc: Create a new post
    params: int topic_id, int parent_id, post_text
    return: int post_id, str post_author, int author_id, post_text, post_date
    """
    response = {
        'success': False,
        'post_id': -1,
        'post_author': '',
        'author_id': -1,
        'post_text': '',
        'post_date': ''
    }
    
    # Validate input
    if valid_request(request):
        topic_id = request.POST['topic_id']
        parent_id = request.POST['parent_id']
        post_text = request.POST['post_text']
        date = timezone.now()
        if topic_id and parent_id and post_text:
            topic = Topic.objects.get(pk=topic_id)
            
            parent = Post.objects.filter(id=parent_id)
            if not parent:
                parent = None
            
            new_post = Post(
                parent=parent,
                text=post_text,
                author=request.user,
                post_date=timezone.now()
            )
            new_post.save()
            
            # Allows you to add the same post to different topics at different
            # points in time.
            relationship = TopicPost.objects.create(
                post=new_post,
                topic=topic,
                date_added=date
            )
            relationship.save()
            topic.last_post = date
            topic.save()
            
            # Set the response
            if new_post.parent:
                response['parent_id'] = new_post.parent.id
            response['post_id'] = new_post.id
            response['post_author'] = new_post.author.username
            response['author_id'] = new_post.author.id
            response['post_text'] = new_post.text
            response['post_date'] = new_post.post_date
            
            # Everything was successful!
            response['success'] = True
    
    # Return results
    return JsonResponse(response)

def modify_post(request):
    pass

def delete_post(request):
    pass
