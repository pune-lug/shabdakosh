from django.conf.urls.defaults import patterns, include, url
from devanagari.api import devanagari_shabda_resource

dsr = devanagari_shabda_resource()

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shabdakosh.views.home', name='home'),
    # url(r'^shabdakosh/', include('shabdakosh.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(dsr.urls)),
)
