from django.contrib import admin
from django.urls import path, re_path
from mainApp import views
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('reservar/<int:id>', views.reservar),
    path('ticket/<int:id>', views.ticket),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT
            }),
    ]
