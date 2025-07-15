from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.dashboard.urls')),
    path('accounts/', include('apps.accounts.urls')),
    path('tracker/', include('apps.tracker.urls')),
    path('medical/', include('apps.medical.urls')),
    path('medicines/', include('apps.medicines.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)