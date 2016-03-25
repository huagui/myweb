# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.


 
from django.utils.encoding import python_2_unicode_compatible
from DjangoUeditor.models import UEditorField
from django.db.models.signals import post_save
from django.contrib.auth.models import User
 
@python_2_unicode_compatible #支持中文
class Profile(models.Model):
	user = models.ForeignKey('auth.User', unique=True)
	nickname = models.CharField('昵称', max_length=20, help_text="请输入昵称", unique=True)
	photo = models.ImageField('头像', upload_to='photo',default='photo/default.jpg')
	birthday = models.DateField('出生日期', blank=True, null=True)
	about = models.CharField('个人简介', blank= True, max_length=20, default='')

	def __str__(self):
		return self.nickname 

	class Meta:
		ordering = ['id']

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

#post_save.connect(create_user_profile, sender=User)


@python_2_unicode_compatible #支持中文
class Blog(models.Model):
	title = models.CharField('标题', max_length=256)
	content = UEditorField('内容', height=1000, width=1000,
 		default=u'', blank=True, imagePath='uploads/images/',
 		toolbars='besttome', filePath='uploads/files')

	author = models.ForeignKey('Profile')
	pub_date = models.DateTimeField('发表时间', auto_now_add=True)
	update_time = models.DateTimeField('更新时间', auto_now=True, null=True)

	def __str__(self):
		return self.title 

	class Meta:
		ordering = ['-pub_date']

	class Admin:
		list_display = ("title")
		# ordering = ["-pub_date"]
		# search_fields = ("job_title", "job_description")
		# list_filter = ("location",)


@python_2_unicode_compatible #支持中文
class Comment(models.Model):
	to_blog = models.ForeignKey('Blog')
	author = models.ForeignKey('Profile')
	pub_date = models.DateTimeField('评论时间', auto_now_add=True)
	content = UEditorField('评论内容', height=200, width=1000,
 		default=u'', blank=True, imagePath='uploads/images/',
 		toolbars='besttome', filePath='uploads/files')

	def __str__(self):
		return self.content

	class Meta:
		ordering = ['-pub_date']

@python_2_unicode_compatible #支持中文
class Msg(models.Model):
	to_user = models.ForeignKey('Profile',related_name='to_user')
	author = models.ForeignKey('Profile', related_name='author')
	pub_date = models.DateTimeField('留言时间', auto_now_add=True)
	content = UEditorField('留言内容', height=200, width=1100,
 		default=u'', blank=True, imagePath='uploads/images/',
 		toolbars='besttome', filePath='uploads/files')

	def __str__(self):
		return self.content

	class Meta:
		ordering = ['-pub_date']

@python_2_unicode_compatible #支持中文
class Photo(models.Model):
	uploader = models.ForeignKey('Profile',related_name='uploader')
	# photo = models.ImageField('头像', upload_to='photo',default='photo/default.jpg')
	image = models.ImageField('相片', upload_to='images', )
	pub_date = models.DateTimeField('上传时间', auto_now_add=True)

	def __str__(self):
		return self.image.url

	class Meta:
		ordering = ['-pub_date']