#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-07-28 20:38:38
# @Author  : Weizhong Tu (mail@tuweizhong.com)
# @Link    : http://www.tuweizhong.com
 
'''
create some records for demo database
'''
 
from myweb.wsgi import *
from blog.models import Blog,Profile
from django.contrib.auth.models import User
 
def main():
    columns= [
      u'a', 
      u'asdfadf', 
      u'fasdfgasdg', 
    ]
    auth = User.objects.get(username="huagui")
    p = Profile.objects.get(user=auth)
    print p.id
   
    for column_name in columns:
        # 创建 10 篇新闻
        for i in range(1, 11):
            blog = Blog(
                title='{}_{}'.format(column_name, i),
                content=u'详细内容： {} {}'.format(column_name, i),
                author = p 
            )
            
            blog.save()
'''
    blog = Blog(
                #title='{}_{}'.format("aaa", 1),
                content='新闻详细内容： {} {}'.format("sssss", 1),
                author = user 
            )
            
    blog.save()
    print(Blog.objects.all())
    print help(Blog)
    #Blog.objects.all().delete()
'''
main()
print("Done!")
