from django.contrib import admin

from models import Profile, Blog, Comment, Msg, Photo
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
	list_dispaly = ('id', 'nickname', 'photo', 'birthday',)
	search_fields = ("nickname", )
	list_filter = ("birthday",)

class BlogAdmin(admin.ModelAdmin):
	list_dispaly = ( "author")
	search_fields = ("author", )
	list_filter = ("pub_date",)


class CommentAdmin(admin.ModelAdmin):
	list_dispaly = ('id', 'to_blog', 'author', 'pub_date')
	search_fields = ("to_blog", "author", 'pub_date')
	list_filter = ("to_blog", 'pub_date')

class MsgAdmin(admin.ModelAdmin):
	list_dispaly = ('id', 'to_user', 'author', 'pub_date')
	search_fields = ("to_user", "author")
	list_filter = ("pub_date",)

class PhotoAdmin(admin.ModelAdmin):
	list_dispaly = ('uploader','image','pub_date')
	search_fields = ("uploader", "image")
	list_filter = ("pub_date",)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Msg, MsgAdmin)
admin.site.register(Photo, PhotoAdmin)
