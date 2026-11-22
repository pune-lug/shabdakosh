from django.contrib import admin
from django.urls import include, path

from shabdakosh.devanagari.api import devanagari_shabda_resource

dsr = devanagari_shabda_resource()

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(dsr.urls)),
]
