from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .serializers import *
from .models import *

# Create your views here.

class ProjectView(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class PostView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class TechnologyView(viewsets.ModelViewSet):
    serializer_class = TechnologySerializer
    queryset = Technology.objects.all()

class TagView(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()

class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class AboutView(viewsets.ModelViewSet):
    serializer_class = AboutSerializer
    queryset = About.objects.all()

class SkillView(viewsets.ModelViewSet):
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()


class ExtraInfoView(viewsets.ModelViewSet):
    serializer_class = ExtraInfoSerializer
    queryset = ExtraInfo.objects.all()

class ClientView(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

class ContactMessageView(viewsets.ModelViewSet):
    serializer_class = ContactMessageSerializer
    queryset = ContactMessage.objects.all()

class ContactInfoView(viewsets.ModelViewSet):
    serializer_class = ContactInfoSerializer
    queryset = ContactInfo.objects.all()