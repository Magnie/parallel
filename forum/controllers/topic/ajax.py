# AJAX for topics

"""
Model Reference

class Topic(models.Model):
    id = models.AutoField(primary_key=True)
    tags = models.ManyToManyField("Tag", symmetrical=False)
    title = models.CharField(max_length=128)
    author = models.ForeignKey(User, blank=True, unique=False)
    permissions = models.ManyToManyField(Permission, blank=True)
    post_date = models.DateTimeField()
    last_post = models.DateTimeField()

    class Meta:
        ordering = ['last_post']
"""

from django.utils import timezone
from django.http import JsonResponse
from forum.models import Tag, Topic, Post, TopicPost, TagTopic
from forum.utils import valid_input, valid_request

def get_topics(request, tag_id):
    """
    desc: Get the topics of a tag
    params: int tag_id
    return: array({int topic_id, str topic_title, topic_author, last_post}) topics
    """
    response = {
        'success': False,
        'topics': []
    }
    
    # Validate input
    if tag_id:
        tag = Tag.objects.get(pk=tag_id)
        if tag:
            
            # Get the topics
            temp_topics = tag.topics.all().order_by('-last_post')
            topics = []
            for t in temp_topics:
                topics.append({
                    'topic_id': t.id,
                    'topic_title': t.title,
                    'topic_author': t.author.username,
                    'last_post': t.last_post.strftime('%a, %d %b %Y %H:%M:%S')
                })
            
            # Set the response
            response['topics'] = topics
            
            # Everything was successful!
            response['success'] = True
    
    # Return results
    return JsonResponse(response)

def create_topic(request):
    """
    desc: Create a new topic
    params: str topic_title, post_text, int tag_id
    return: bool success, int topic_id, str topic_title, str topic_author
    """
    response = {
        'success': False,
        'topic_id': -1,
        'topic_title': '',
        'topic_author': '',
        'topic_date': '',
    }

    # Validate input
    if valid_request(request):
        topic_title = request.POST['topic_title']
        tag_id = request.POST['tag_id']
        post_text = request.POST['post_text']
        date = timezone.now()
        if topic_title and tag_id and post_text:
            tag = Tag.objects.get(pk=tag_id)
            new_topic = Topic(
                title=topic_title,
                author=request.user,
                post_date=date,
                last_post=date
            )
            new_topic.save()
            
            tag_topic = TagTopic.objects.create(
                tag=tag,
                topic=new_topic,
                date_added=date
            )
            tag_topic.save()
            
            new_post = Post(
                text=post_text,
                author=request.user,
                post_date=date
            )
            new_post.save()
            
            topic_post = TopicPost.objects.create(
                topic=new_topic,
                post=new_post,
                date_added=date
            )
            
            # Set the response
            response['topic_id'] = new_topic.id
            response['topic_title'] = new_topic.title
            response['topic_author'] = new_topic.author.username
            response['topic_date'] = date
            
            # Everything was successful!
            response['success'] = True

    # Return results
    return JsonResponse(response)

def modify_topic(request):
    """
    desc: Modify a topic
    params: str action (name,), value (str name,)
    return: bool success
    """
    pass

def delete_topic(request):
    """
    desc: Delete a topic
    params: int topic_id
    return: bool success
    """
    pass
