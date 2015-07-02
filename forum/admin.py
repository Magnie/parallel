from django.contrib import admin

# Register your models here.
from .models import Tag, Topic, Post, FUser, FGroup, FPermission

admin.site.register(Tag)
admin.site.register(Topic)
admin.site.register(Post)
admin.site.register(FUser)
admin.site.register(FGroup)
admin.site.register(FPermission)
