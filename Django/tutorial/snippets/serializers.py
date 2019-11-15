#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
'''
@Filename  :   serializers.py
@Time      :   2019/10/23
@Team      :   None
@Author    :   Jqiu qiuyue
@Contact   :   qiuyue77@outlook.com
@Tool      :   PyCharm
'''
# here put the import lib
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User
class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner')


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')