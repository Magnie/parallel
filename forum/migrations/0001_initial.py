# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='FGroup',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='FPermission',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='FUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('groups', models.ManyToManyField(to='forum.FGroup', blank=True)),
                ('permissions', models.ManyToManyField(to='forum.FPermission', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('text', models.TextField()),
                ('post_date', models.DateTimeField()),
                ('author', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('parent', models.ForeignKey(blank=True, to='forum.Post', null=True)),
            ],
            options={
                'ordering': ['post_date'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32)),
                ('groups', models.ManyToManyField(to='forum.FGroup', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('post_date', models.DateTimeField()),
                ('last_post', models.DateTimeField()),
                ('author', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('permissions', models.ManyToManyField(to='auth.Permission', blank=True)),
                ('tags', models.ManyToManyField(to='forum.Tag')),
            ],
            options={
                'ordering': ['last_post'],
            },
        ),
        migrations.AddField(
            model_name='tag',
            name='itopics',
            field=models.ManyToManyField(to='forum.Topic', blank=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='permissions',
            field=models.ManyToManyField(to='forum.FPermission', blank=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='tags',
            field=models.ManyToManyField(to='forum.Tag', blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='topics',
            field=models.ManyToManyField(to='forum.Topic'),
        ),
        migrations.AddField(
            model_name='fgroup',
            name='permissions',
            field=models.ManyToManyField(to='forum.FPermission', blank=True),
        ),
    ]
