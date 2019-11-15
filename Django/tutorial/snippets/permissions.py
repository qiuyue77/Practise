#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
'''
@Filename  :   permissions.py
@Time      :   2019/10/24
@Team      :   None
@Author    :   Jqiu qiuyue
@Contact   :   qiuyue77@outlook.com
@Tool      :   PyCharm
'''
# here put the import lib
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    自定义权限只允许对象的所有者编辑它。
    """
    def has_object_permission(self, request, view, obj):
        # 读取权限允许任何请求，
        # 所以我们总是允许GET，HEAD或OPTIONS请求。
        if request.method in permissions.SAFE_METHODS:
            return True

        # 只有该snippet的所有者才允许写权限。
        return obj.owner == request.user