from django.contrib import admin
from django.urls import path, include # Import include here
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('src.urls')), # This directs all traffic to your src app
]

# This allows the browser to see the uploaded images
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)