# -*- coding:utf-8 -*-
from rest_framework import viewsets, permissions

from main.models import TodoList
from django.contrib.auth.models import User
from .serializers import UserSerializer, TodoListSerializer


class IsCreatorOrReadOnly(permissions.BasePermission):
    """
    只允许创建者修改但允许所有人读的权限设置
    """
    def has_object_permission(self, request, view, obj):
        # 所有用户都允许读取,所以安全的http方法会直接放行
        # SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
        if request.method in permissions.SAFE_METHODS:
            return True
        # 写入权限需要创建者本人
        return obj.creator == request.user

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    处理 /api/users/ GET, 处理 /api/users/<pk>/ GET
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)

class TodoListViewSet(viewsets.ModelViewSet):
    """
    处理 /api/todolists/ GET POST , 处理 /api/todolists/<pk>/ GET PUT PATCH DELETE
    """
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    permission_classes = (IsCreatorOrReadOnly,)
    
    def perform_create(self, serializer):
        """
        重写 perform_create
        user 信息不在 request.data 中, 在保存时加入 user 信息
        """
        user = self.request.user
        creator = user if user.is_authenticated else None
        serializer.save(creator=creator)
