import imp
from turtle import title
from attr import fields
from rest_framework import serializers
from .models import Posts

class PostsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Posts
        fields = ('title','content')