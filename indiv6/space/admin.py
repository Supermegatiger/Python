from django.contrib import admin
from .models import *


# Register your models here.
class GalaxyTypeAdmin(admin.ModelAdmin):
    t = ['name']
    list_display = t
    list_display_links = t
    list_filter = t
    search_fields = t

    class Meta:
        model = GalaxyType


class GalaxyAdmin(admin.ModelAdmin):
    t = ['name', 'age', 'size']
    list_display = t
    list_display_links = t
    list_filter = t
    search_fields = t
    # fields = ('first_name', 'second_name', 'email')

    class Meta:
        model = Galaxy


class StarSystemAdmin(admin.ModelAdmin):
    t = ['name', 'age', 'radius']
    list_display = t
    list_display_links = t
    list_filter = t
    search_fields = t
    # fields = ('first_name', 'second_name', 'email')

    class Meta:
        model = StarSystem


class PlanetAdmin(admin.ModelAdmin):
    t = ['name', 'age', 'radius', 'mass', 'habitable']
    list_display = t
    list_display_links = t
    list_filter = t
    search_fields = t
    # fields = ('first_name', 'second_name', 'email')

    class Meta:
        model = Planet


class StarAdmin(admin.ModelAdmin):
    t = ['name', 'age', 'radius', 'mass', 'temperature']
    list_display = t
    list_display_links = t
    list_filter = t
    search_fields = t
    # fields = ('first_name', 'second_name', 'email')

    class Meta:
        model = Star


admin.site.register(GalaxyType, GalaxyTypeAdmin)
admin.site.register(Galaxy, GalaxyAdmin)
admin.site.register(StarSystem, StarSystemAdmin)
admin.site.register(Planet, PlanetAdmin)
admin.site.register(Star, StarAdmin)
