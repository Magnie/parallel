# Views for tags.
from django.shortcuts import render
from django.contrib import auth
from django.utils import timezone

from django.db import models
from forum.models import Tag, Topic, Post

from django.shortcuts import get_object_or_404

def tag(request, tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)
    data = {
        'view': 'forum/views/tag.html',
        'tag_id': tag.id,
        'id': tag.id,
        'page': 'tag',
        'tag_name': tag.name
    }
    return render(request, 'forum/container.html', data)
