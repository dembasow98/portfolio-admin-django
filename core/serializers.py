from rest_framework import serializers
from .models import *

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'id', 
            'user', 
            'title', 
            'objective',
            'thumbnail',
            'technologies',
            'categories',
            'tags',
            'images',
            'status',
            'live_link',
            'source_link',
            'created_at',
            'updated_at',
        )