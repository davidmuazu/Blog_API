from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    #displays the user name of the authorinstead of the user id when retrieving posts

    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at', 'updated_at']
        read_only_fields = ['author', 'created_at', 'updated_at']
        
