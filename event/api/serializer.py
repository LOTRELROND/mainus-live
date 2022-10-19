from rest_framework import serializers
from event.models import Post,Author,Category,Reply,Comment



class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields ='__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        categories = CategorySerializer(many=True, read_only=True)
        model = Post
        fields='__all__'