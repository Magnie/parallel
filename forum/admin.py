from django.contrib import admin

# Register your models here.
from .models import Tag, Topic, Post, ForumUser, TopicPost, TagTopic

admin.site.register(Tag)
admin.site.register(TagTopic)
admin.site.register(Topic)
admin.site.register(TopicPost)
admin.site.register(Post)
admin.site.register(ForumUser)
