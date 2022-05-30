from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('api/v1/panel/brx/', admin.site.urls),
    path('api/v1/blog/', include('blog.urls', namespace='blog')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('bxlanding.urls')),
    path('api/v1/auth-data/', include('authorization.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
