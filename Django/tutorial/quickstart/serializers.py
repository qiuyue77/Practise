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
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
