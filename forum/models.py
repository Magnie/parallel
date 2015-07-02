from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth.models import User, Permission

# Create your models here.


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, unique=True)
    tags = models.ManyToManyField("self", blank=True, symmetrical=False)
    itopics = models.ManyToManyField("Topic", blank=True)
    
    groups = models.ManyToManyField("FGroup", blank=True)
    permissions = models.ManyToManyField("FPermission", blank=True)
    
    def __unicode__(self):
       return self.name


class Topic(models.Model):
    id = models.AutoField(primary_key=True)
    tags = models.ManyToManyField("Tag", symmetrical=False)
    title = models.CharField(max_length=128)
    author = models.ForeignKey(User, unique=False)
    post_date = models.DateTimeField()
    last_post = models.DateTimeField()
    
    permissions = models.ManyToManyField(Permission, blank=True)
    
    def __unicode__(self):
       return self.title

    class Meta:
        ordering = ['last_post']


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    parent = models.ForeignKey('Post', null=True, blank=True, unique=False) # Allows for microthreads
    topics = models.ManyToManyField("Topic")
    text = models.TextField()
    author = models.ForeignKey(User, unique=False)
    post_date = models.DateTimeField()
    
    def __unicode__(self):
        return self.text
    
    class Meta:
        ordering = ['post_date']


class FUser(models.Model):
    user = models.OneToOneField(User)
    permissions = models.ManyToManyField("FPermission", symmetrical=False, blank=True)
    groups = models.ManyToManyField("FGroup", symmetrical=False, blank=True)
    
    def __unicode__(self):
        return self.user

def username_check(sender, instance, **kwargs):
    "Enforce lowercase usernames."
    if User.objects.filter(username=instance.username.lower()).count():
       pass

pre_save.connect(username_check, sender=User)


class FGroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, unique=True)
    permissions = models.ManyToManyField("FPermission", symmetrical=False, blank=True)
    
    def __unicode__(self):
        return self.name


class FPermission(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, unique=True)
    
    def __unicode__(self):
        return self.name
