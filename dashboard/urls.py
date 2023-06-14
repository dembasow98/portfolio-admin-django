from django.contrib import admin
from django.urls import path
from django.urls import include

from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = "ZERO EXCUSES"
admin.site.site_title = "ZERO EXCUSES ADMINISTRATION PANEL"
admin.site.index_title  = "ZERO EXCUSES ADMINISTRATION PANEL"
#

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
