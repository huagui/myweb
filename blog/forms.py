# -*- coding: utf-8 -*-
from django import forms
from blog.models import Profile, Blog, Comment, Msg, Photo
from django.forms import ModelForm


class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		fields = ['nickname', 'photo', 'birthday', 'about']
	def clean_about(self):
		about = self.cleaned_data['about']
		if 'huagui' not in about:
			raise forms.ValidationError('my error')
		return about
		
			


class BlogForm(ModelForm):
	class Meta:
		model = Blog
		fields = ['title', 'content']

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ['content']

class MsgForm(ModelForm):
	class Meta:
		model = Msg
		fields = ['content']

class PhotoForm(ModelForm):
	class Meta:
		model = Photo
		fields = ['image']