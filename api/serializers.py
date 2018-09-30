from rest_framework import serializers
from django.contrib.auth.models import User
from main.models import TodoList


class UserSerializer(serializers.ModelSerializer):

    todolists = serializers.PrimaryKeyRelatedField(
        many=True, queryset=TodoList.objects.all()
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'todolists')

class TodoListSerializer(serializers.ModelSerializer):

    creator = serializers.ReadOnlyField(source='creator.username')
    
    class Meta:
        model = TodoList
        fields = ('id', 'title', 'created_date', 'creator')

