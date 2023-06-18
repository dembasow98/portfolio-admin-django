from django.contrib import admin

# Register your models here.


from core.models import (
    Post, 
    Project, 
    Social, 
    Image, 
    Client, 
    About, 
    ContactMessage, 
    ContactInfo,
    TrustBrand, 
    ExtraInfo, 
    Skill,
    Tag, 
    Category,
    Technology,
)


@admin.register(ExtraInfo)
class ExtraInfo(admin.ModelAdmin):
    pass

@admin.register(Technology)
class Technology(admin.ModelAdmin):
    pass

@admin.register(Skill)
class Skill(admin.ModelAdmin):
    pass

@admin.register(Tag)
class Tag(admin.ModelAdmin):
    pass

@admin.register(Category)
class Category(admin.ModelAdmin):
    pass


@admin.register(Client)
class Client(admin.ModelAdmin):
    pass

@admin.register(About)
class About(admin.ModelAdmin):
    pass

@admin.register(ContactMessage)
class ContactMessage(admin.ModelAdmin):
    pass

@admin.register(ContactInfo)
class ContactInfo(admin.ModelAdmin):
    pass

@admin.register(TrustBrand)
class TrustBrand(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass