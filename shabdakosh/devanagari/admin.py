from django.contrib import admin

from shabdakosh.devanagari.models import shabda


class shabda_admin(admin.ModelAdmin):
    list_display = ('shabda', 'kiti_vela')
    ordering = ['shabda', ]
    search_fields = ('shabda', )


admin.site.register(shabda, shabda_admin)
