from django.contrib import admin

# Register your models here.


from core.models import Post, Project, Category, Technology, Tool, Social


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    pass


@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    pass

@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass