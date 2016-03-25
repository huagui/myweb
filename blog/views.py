# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext  

from a import log as mylog
# Create your views here.
from models import Profile
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required 
from blog.forms import ProfileForm, BlogForm, CommentForm, MsgForm, PhotoForm
from blog.models import Blog, Profile ,Comment, Msg, Photo
from django.contrib.auth import logout,get_user

import huagui


def logout(request):
    logout(request)
    return HttpResponseRedirect("/")

def index(request):
    return render_to_response('blog/index.html')


@login_required
def upload_photo(request, host_id):
    if request.user.is_authenticated(): #是否登陆
        user = request.user
        user_pro = Profile.objects.get(user=user) 
        is_host = True
        if request.method == 'POST': #是否为post
            photoform = PhotoForm(request.POST,request.FILES)
            if photoform.is_valid():
                # mylog('is_valid')
                image = photoform.cleaned_data['image']
                # mylog(image.url)
                new_photo = Photo(
                                    uploader=user_pro,
                                    image=image
                                    )
                new_photo.save()
                return HttpResponseRedirect("/blog/{}/photo".format(host_id))
                # return HttpResponseRedirect("/blog/" + str(host_id) + 'detail')
            else:
                mylog('is_not_valid')
            
            return HttpResponseRedirect("/blog/{}/photo".format(host_id))

        
        else:
            photoform = PhotoForm()
        return render(request, 'blog/upload_photo.html', 
                              {'user_pro':user_pro, 'is_host':is_host,
                                'photoform':photoform,}
                        )
        # return render_to_response('blog/upload_photo.html', 
        #             {'user_pro':user_pro, 'is_host':is_host, 'photoform':photoform,} 
        #             , context_instance=RequestContext(request))
    else:
        return render_to_response("aaa")


@login_required
def pro(request, host_id):
    if request.user.is_authenticated():
                user = request.user
                blogger = User.objects.get(id = host_id)
                host_pro = Profile.objects.get(user=blogger) #博主 
                user_pro = Profile.objects.get(user=user) #登陆的用户
                if user == blogger: #如果登陆的用户为博主
                    is_host = True
                else:
                    is_host = False 
                return render(request, 'blog/pro_info.html', {'host_pro':host_pro, 'user_pro':user_pro, 'is_host':is_host})
    else:
                return render_to_response("eee")


@login_required
def photo(request, host_id):
    if request.user.is_authenticated():
                user = request.user
                blogger = User.objects.get(id = host_id)
                host_pro = Profile.objects.get(user=blogger) #博主 
                user_pro = Profile.objects.get(user=user) #登陆的用户
                photo_list = Photo.objects.filter(uploader=host_pro)
                if user == blogger: #如果登陆的用户为博主
                    is_host = True
                else:
                    is_host = False 
                return render(request, 'blog/photo.html', {'host_pro':host_pro, 'user_pro':user_pro, 'is_host':is_host, 'photo_list':photo_list})
    else:
                return render_to_response("eee")

    # return render(request, '/blog/friend.html')

@login_required
def friend(request, host_id):
    if request.user.is_authenticated():
                user = request.user
                blogger = User.objects.get(id = host_id)
                host_pro = Profile.objects.get(user=blogger) #博主 
                user_pro = Profile.objects.get(user=user) #登陆的用户
                friend_list = Profile.objects.all()
                if user == blogger: #如果登陆的用户为博主
                    is_host = True
                else:
                    is_host = False 
                return render(request, 'blog/friend.html', {'host_pro':host_pro, 'user_pro':user_pro, 'is_host':is_host, 'friend_list':friend_list})
    else:
                return render_to_response("eee")

    # return render(request, '/blog/friend.html')

@login_required
def msg(request, host_id):

    if request.user.is_authenticated(): #是否登陆

        user = request.user
        blogger = User.objects.get(id = host_id)
        host_pro = Profile.objects.get(user=blogger) #博主 
        user_pro = Profile.objects.get(user=user) #登陆的用户
        msg_list = Msg.objects.filter(to_user=host_pro)

        if user == blogger: #如果登陆的用户为博主
            is_host = True
        else:
            is_host = False 

        if request.method == 'POST': #是否为post
            msgform = MsgForm(request.POST)
            if msgform.is_valid():
                content = msgform.cleaned_data['content']
                new_msg = Msg(
                                    to_user=host_pro,
                                    author=user_pro,
                                    content=content,
                                    )
                new_msg.save()
                return HttpResponseRedirect("/blog/{}/msg".format(host_id))
                # return HttpResponseRedirect("/blog/" + str(host_id) + 'detail')
        
        else:
            msgform = MsgForm()
            # return render(request, 'blog/msg.html')
        return render(request, 'blog/msg.html', 
                              {'host_pro':host_pro, 'user_pro':user_pro, 'is_host':is_host, 'msg_list':msg_list,
                                'msgform':msgform,}
                        )
    else:
        return render_to_response("aaa")

@login_required
def host(request):

    if request.user.is_authenticated():
                user = request.user
                # blogger = User.objects.get(id = host_id)
                # host_pro = Profile.objects.get(user=blogger) #博主 
                user_pro = Profile.objects.get(user=user) #登陆的用户
                is_host = True 
                return render(request, 'blog/home.html', {'host_pro':user_pro, 'user_pro':user_pro, 'is_host':is_host })
    else:
                return render_to_response("eee")


@login_required
def add(request,host_id):
    if request.method == 'POST':
        blogform = BlogForm(request.POST)
       
        if blogform.is_valid():
            title = blogform.cleaned_data['title']
            content = blogform.cleaned_data['content']
            author = Profile.objects.get(user=request.user)
            new_blog = Blog(
                              author=author,
                              title=title,
                              content=content,
                              )
            new_blog.save()
            return HttpResponseRedirect("/blog/"+str(request.user.id) )
        
    else:
        blogform = BlogForm()
    return render_to_response("blog/add_blog.html", {'blogform': blogform}, context_instance=RequestContext(request))

@login_required
def home(request,host_id):
	if request.user.is_authenticated():
                user = request.user
                blogger = User.objects.get(id = host_id)
                host_pro = Profile.objects.get(user=blogger) #博主 
                user_pro = Profile.objects.get(user=user) #登陆的用户
                if user == blogger: #如果登陆的用户为博主
                    is_host = True
                else:
                    is_host = False 
                return render(request, 'blog/home.html', {'host_pro':host_pro, 'user_pro':user_pro, 'is_host':is_host })
        else:
                return render_to_response("eee")


@login_required
def detail(request, host_id, pk):

    if request.user.is_authenticated(): #是否登陆
        user = request.user
        blogger = User.objects.get(id = host_id)
        host_pro = Profile.objects.get(user=blogger) #博主 
        user_pro = Profile.objects.get(user=user) #登陆的用户
        blog = Blog.objects.get(pk=pk)
        comment_list = Comment.objects.filter(to_blog=blog)

        if user == blogger: #如果登陆的用户为博主
            is_host = True
        else:
            is_host = False 

        if request.method == 'POST': #是否为post
            commentform = CommentForm(request.POST)
            if commentform.is_valid():
                content = commentform.cleaned_data['content']
                new_comment = Comment(
                                    to_blog=blog,
                                    author=user_pro,
                                    content=content,
                                    )
                new_comment.save()
                return HttpResponseRedirect("/blog/{}/detail/{}".format(host_id, blog.id))
                # return HttpResponseRedirect("/blog/" + str(host_id) + 'detail')
        
        else:
            commentform = CommentForm()
        return render(request, 'blog/blog_detail.html', 
                              {'host_pro':host_pro, 'user_pro':user_pro, 'is_host':is_host , 'blog':blog, 'comment_list':comment_list,
                                'commentform':commentform,}
                        )
        # return render_to_response("blog/blog_detail.html", {'userform': userform,'proform':proform }, context_instance=RequestContext(request))

    else:
        return render_to_response("eee")

    

    

@login_required
def list(request,host_id): #显示日志列表
    if request.user.is_authenticated():
        user = request.user
        blogger = User.objects.get(id = host_id)
        host_pro = Profile.objects.get(user=blogger)
        blog_list = Blog.objects.filter(author=host_pro)
        user_pro = Profile.objects.get(user=user) #登陆的用户
        if user == blogger: #如果登陆的用户为博主
            is_host = True
        else:
            is_host = False 

        
        objects, page_range = huagui.my_pagination(request, blog_list)
        return render(request, 'blog/list.html', 
                        {'objects':objects,'page_range':page_range,
                        'host_pro':host_pro, 'blog_list':blog_list,
                        'user_pro':user_pro, 'is_host':is_host}
                        )
    else:
        return render_to_response("eee")
    
@csrf_protect
def register(request):
    if request.method == 'POST':
        userform = UserCreationForm(request.POST)
        proform = ProfileForm(request.POST,request.FILES)
        # if userform.is_valid():
        #     new_user = userform.save()
        # else:
        #     for f in userform:
        #         mylog(str(f))
        # if proform.is_valid():
        #     new_pro = proform.save()
        #     return HttpResponseRedirect("/")
        if userform.is_valid() and proform.is_valid():
            new_user = userform.save()
            
            nickname = proform.cleaned_data['nickname']
            photo = proform.cleaned_data['photo']
            birthday = proform.cleaned_data['birthday']
            about = proform.cleaned_data['about']

            new_pro = Profile(
                              user=new_user,
                              nickname=nickname,
                              photo=photo,
                              birthday=birthday,
                              about=about  )
            new_pro.save()
            return HttpResponseRedirect("/")
        
    else:
        userform = UserCreationForm()
        proform = ProfileForm()
    return render_to_response("blog/register.html", {'userform': userform,'proform':proform }, context_instance=RequestContext(request))
    # user = User.objects.create_user(username='john',
    #                           email='jlennon@beatles.com',
    #                             password='glass onion')

    # user.is_staff = True
    # user.save()


