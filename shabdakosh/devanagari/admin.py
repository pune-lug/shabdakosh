from shabdakosh.devanagari.models import *
from django.contrib import admin


class shabda_admin(admin.ModelAdmin):
    list_display = ('shabda', 'kiti_vela')
    ordering = ['shabda', ]
    search_fields = ('shabda', )
    

admin.site.register(shabda, shabda_admin)
