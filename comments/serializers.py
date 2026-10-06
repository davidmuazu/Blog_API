from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    #displays the user name of the author instead of the user id when retrieving comments

    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'content', 'author', 'post', 'created_at', 'updated_at']
        read_only_fields = ['author', 'created_at', 'updated_at']