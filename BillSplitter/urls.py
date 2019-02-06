"""BillSplitter URL Configuration"""

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

import BillSplitter.views as local_views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', local_views.index, name='index'),
    path('dashboard/', include('splitter.urls')),
    path('users/', include('users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)