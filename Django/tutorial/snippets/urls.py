#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
'''
@Filename  :   urls.py
@Time      :   2019/10/23
@Team      :   None
@Author    :   Jqiu qiuyue
@Contact   :   qiuyue77@outlook.com
@Tool      :   PyCharm
'''
# here put the import lib
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    url(r'^user/$', views.UserList.as_view()),
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)