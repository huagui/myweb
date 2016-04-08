# -*- coding: utf-8 -*-
from django.contrib import admin

from models import Profile, Blog, Comment, Msg, Photo ,Author, Video
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
	list_display = ('id', 'nickname', 'photo', 'birthday',)
	search_fields = ("nickname",'id' )
	list_filter = ("birthday",)

class BlogAdmin(admin.ModelAdmin):
	list_display = ( "author",'title', 'pub_date','content', )
	search_fields = ("author__nickname", 'title','content')
	list_filter = ("pub_date",'author',)
	fields = ('title','content') #允许在admin中修改的字段


class CommentAdmin(admin.ModelAdmin):
	list_display = ('id', 'to_blog', 'author', 'pub_date')
	search_fields = ("to_blog", "author", 'pub_date')
	list_filter = ("to_blog", 'pub_date')

class MsgAdmin(admin.ModelAdmin):
	list_display = ('id', 'to_user', 'author', 'pub_date')
	search_fields = ("to_user", "author")
	list_filter = ("pub_date",)

class PhotoAdmin(admin.ModelAdmin):
	list_display = ('uploader','image','pub_date')
	search_fields = ("uploader", "image")
	list_filter = ("pub_date",)

class VideoAdmin(admin.ModelAdmin):
	list_display = ('uploader','path','pub_date')
	search_fields = ('uploader','path')
	list_filter=('uploader','pub_date')


admin.site.register(Blog, BlogAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Msg, MsgAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Video,VideoAdmin)
