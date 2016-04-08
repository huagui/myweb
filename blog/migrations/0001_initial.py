# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import DjangoUeditor.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, verbose_name='\u6807\u9898')),
                ('content', DjangoUeditor.models.UEditorField(default='', verbose_name='\u5185\u5bb9', blank=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u8868\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4', null=True)),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='\u8bc4\u8bba\u65f6\u95f4')),
                ('content', DjangoUeditor.models.UEditorField(default='', verbose_name='\u8bc4\u8bba\u5185\u5bb9', blank=True)),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Msg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='\u7559\u8a00\u65f6\u95f4')),
                ('content', DjangoUeditor.models.UEditorField(default='', verbose_name='\u7559\u8a00\u5185\u5bb9', blank=True)),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(default='', upload_to='images', verbose_name='\u76f8\u7247')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='\u4e0a\u4f20\u65f6\u95f4')),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nickname', models.CharField(help_text='\u8bf7\u8f93\u5165\u6635\u79f0', unique=True, max_length=20, verbose_name='\u6635\u79f0')),
                ('photo', models.ImageField(default='photo/default.jpg', upload_to='photo', verbose_name='\u5934\u50cf')),
                ('birthday', models.DateField(null=True, verbose_name='\u51fa\u751f\u65e5\u671f', blank=True)),
                ('about', models.CharField(default='', max_length=20, verbose_name='\u4e2a\u4eba\u7b80\u4ecb', blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='photo',
            name='uploader',
            field=models.ForeignKey(related_name='uploader', to='blog.Profile'),
        ),
        migrations.AddField(
            model_name='msg',
            name='author',
            field=models.ForeignKey(related_name='author', to='blog.Profile'),
        ),
        migrations.AddField(
            model_name='msg',
            name='to_user',
            field=models.ForeignKey(related_name='to_user', to='blog.Profile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(to='blog.Profile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='to_blog',
            field=models.ForeignKey(to='blog.Blog'),
        ),
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(to='blog.Profile'),
        ),
    ]
