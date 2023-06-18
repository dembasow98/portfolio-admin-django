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

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id', 
            'user', 
            'title',
            'status',
            'content',
            'thumbnail',
            'categories',
            'tags',
            'summary',
            'created_at',
            'updated_at',
        )

class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = (
            'id', 
            'user',
            'name', 
            'description',
            'created_at',
            'updated_at',
        )

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'id', 
            'user',
            'name', 
            'created_at',
            'updated_at',
        )

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id', 
            'user',
            'name', 
            'created_at',
            'updated_at',
        )


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = (
            'id', 
            'user',
            'profile_picture',
            'images',
            'about',
            'skills',
            'cv',
            'extra_info',
            'trust_brands',
            'clients',
            'contact',
            'created_at',
            'updated_at',
        )

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = (
            'id', 
            'user',
            'name',
            'description',
            'link',
            'created_at',
            'updated_at',
        )

class ExtraInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraInfo
        fields = (
            'id', 
            'user',
            'years_of_experience',
            'github_stars',
            'projects_completed',
            'positive_feedback',
            'happy_clients',
            'cups_of_coffee',
            'created_at',
            'updated_at',
        )

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            'id', 
            'user',
            'profile',
            'name',
            'surname',
            'job',
            'nationality',
            'feedback',
            'created_at',
            'updated_at',
        )


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = (
            'id', 
            'user',
            'full_name',
            'email',
            'subject',
            'message',
            'created_at',
            'updated_at',
        )

class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = (
            'id', 
            'user',
            'address',
            #'phone',
            'email',
            'map_location',
            'created_at',
            'updated_at',
        )

class TrustBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrustBrand
        fields = (
            'id', 
            'user',
            'name',
            'image',
            'link',
            'created_at',
            'updated_at',
        )


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (
            'id', 
            'user',
            'title',
            'image',
            'created_at',
            'updated_at',
        )

class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = (
            'id', 
            'user',
            'name',
            'link',
            'logo',
            'created_at',
            'updated_at',
        )