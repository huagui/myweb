# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160328_2004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.FileField(upload_to='videos', verbose_name='\u89c6\u9891')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='\u4e0a\u4f20\u65f6\u95f4')),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(verbose_name='\u5bf9\u5e94\u7684\u5185\u7f6eUser', to=settings.AUTH_USER_MODEL, unique=True),
        ),
        migrations.AddField(
            model_name='video',
            name='uploader',
            field=models.ForeignKey(related_name='uploader_of_video', to='blog.Profile'),
        ),
    ]
