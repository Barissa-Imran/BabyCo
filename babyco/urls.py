from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('core.urls')),
    path('shop/', include('shop.urls')),
    path('shop/users/', include('users.urls')),

    #   media url
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]

urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)

