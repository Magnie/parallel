from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth.models import User, Permission

# Create your models here.


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, unique=True)
    tags = models.ManyToManyField("self", blank=True, symmetrical=False)
    itopics = models.ManyToManyField(
        "Topic",
        blank=True,
        related_name='itopics'
    )
    topics = models.ManyToManyField(
        'Topic',
        through='TagTopic',
        related_name='topics'
    )
    
    def __unicode__(self):
       return self.name


class Topic(models.Model):
    id = models.AutoField(primary_key=True)
    posts = models.ManyToManyField('Post', through='TopicPost')
    title = models.CharField(max_length=128)
    author = models.ForeignKey(User, unique=False)
    post_date = models.DateTimeField()
    last_post = models.DateTimeField()
    
    def __unicode__(self):
       return self.title

    class Meta:
        ordering = ['last_post']

class TagTopic(models.Model):
    "Tag to Topic relationship"
    topic = models.ForeignKey('Topic')
    tag = models.ForeignKey('Tag')
    date_added = models.DateTimeField(blank=True)
    
    class Meta:
        ordering = ('date_added',)


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    parent = models.ForeignKey('self', null=True, blank=True, unique=False) # Allows for microthreads
    text = models.TextField()
    author = models.ForeignKey(User, unique=False)
    post_date = models.DateTimeField()
    
    def __unicode__(self):
        return self.text
    
    class Meta:
        ordering = ['post_date']

class TopicPost(models.Model):
    "Topic to Post relationship"
    post = models.ForeignKey('Post')
    topic = models.ForeignKey('Topic')
    date_added = models.DateTimeField()
    
    class Meta:
        ordering = ('date_added',)


class ForumUser(models.Model):
    user = models.OneToOneField(User)
    
    def __unicode__(self):
        return self.user

def username_check(sender, instance, **kwargs):
    "Enforce lowercase usernames."
    if User.objects.filter(username=instance.username.lower()).count():
       pass

pre_save.connect(username_check, sender=User)
