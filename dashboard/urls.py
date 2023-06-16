from django.contrib import admin
from django.urls import path
from django.urls import include

from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers
from core.views import *

admin.site.site_header = "ZERO EXCUSES"
admin.site.site_title = "ZERO EXCUSES ADMINISTRATION PANEL"
admin.site.index_title  = "ZERO EXCUSES ADMINISTRATION PANEL"


router = routers.DefaultRouter()
router.register(r'projects', ProjectView, 'project')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api/', include(router.urls)),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
