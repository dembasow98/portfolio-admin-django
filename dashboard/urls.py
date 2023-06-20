from django.contrib import admin
from django.urls import path
from django.urls import include

from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers
from core.views import *

from core.urls import *



# Require login to access admin panel
#from django.contrib.auth.decorators import login_required
#admin.autodiscover()
#admin.site.login = login_required(admin.site.login)


admin.site.site_header = "ZERO EXCUSES"
admin.site.site_title = "ZERO EXCUSES ADMINISTRATION PANEL"
admin.site.index_title  = "ZERO EXCUSES ADMINISTRATION PANEL"


router = routers.DefaultRouter()
router.register(r'projects', ProjectView, 'project')
router.register(r'posts', PostView, 'post')
router.register(r'technologies', TechnologyView, 'technology')
router.register(r'tags', TagView, 'tag')
router.register(r'categories', CategoryView, 'category')
router.register(r'about', AboutView, 'about')
router.register(r'skills', SkillView, 'skill')
router.register(r'extra-info', ExtraInfoView, 'extra-info')
router.register(r'clients', ClientView, 'client')
router.register(r'contact-messages', ContactMessageView, 'contact-message')
router.register(r'contact-info', ContactInfoView, 'contact-info')



urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api/v1.0.0/', include(router.urls)),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
