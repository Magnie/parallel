# Views for tags.
from django.shortcuts import render
from django.contrib import auth
from django.utils import timezone

from django.db import models
from forum.models import Tag, Topic, Post

from django.shortcuts import get_object_or_404

def topic(request, topic_id, offset=0):
    topic = get_object_or_404(Topic, pk=topic_id)
    data = {
        'view': 'forum/views/topic.html',
        'topic_id': topic.id,
        'id': topic.id,
        'page': 'topic',
        'page_num': offset,
        'topic_title': topic.title
    }
    return render(request, 'forum/container.html', data)
