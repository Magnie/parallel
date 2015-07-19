# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_auto_20150629_1354'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagTopic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_added', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TopicPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_added', models.DateTimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='topics',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='tags',
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=None, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tag',
            name='itopics',
            field=models.ManyToManyField(related_name='itopics', to='forum.Topic', blank=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='topicpost',
            name='post',
            field=models.ForeignKey(to='forum.Post'),
        ),
        migrations.AddField(
            model_name='topicpost',
            name='topic',
            field=models.ForeignKey(to='forum.Topic'),
        ),
        migrations.AddField(
            model_name='tagtopic',
            name='tag',
            field=models.ForeignKey(to='forum.Tag'),
        ),
        migrations.AddField(
            model_name='tagtopic',
            name='topic',
            field=models.ForeignKey(to='forum.Topic'),
        ),
        migrations.AddField(
            model_name='tag',
            name='topics',
            field=models.ManyToManyField(related_name='topics', through='forum.TagTopic', to='forum.Topic'),
        ),
        migrations.AddField(
            model_name='topic',
            name='posts',
            field=models.ManyToManyField(to='forum.Post', through='forum.TopicPost'),
        ),
    ]
