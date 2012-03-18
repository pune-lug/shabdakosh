from tastypie.resources import ModelResource
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from devanagari.models import shabda


class devanagari_shabda_resource(ModelResource):
    class Meta:
        queryset = shabda.objects.all()
        resource_name = 'devanagari'
        excludes = ['id', 'kiti_vela']
        allowed_methods = ['get']
        filtering = {
            'shabda': ALL,
        }

