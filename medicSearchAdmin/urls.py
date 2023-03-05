from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static, settings

urlpatterns = [
    path('', include('medicSearch.urls.HomeUrls')),
    path('admin/', admin.site.urls),
    path('profile/', include('medicSearch.urls.ProfileUrls'))
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    ) + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
