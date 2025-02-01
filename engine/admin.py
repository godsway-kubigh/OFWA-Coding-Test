from django.contrib import admin
from .models import GalamsaySite, GalamsayAnalysis


class GalamsaySiteAdmin(admin.ModelAdmin):
    list_display = ('city', 'region', 'number_of_sites')
    search_fields = ('city', 'region')
    list_filter = ('region',)


class GalamsayAnalysisAdmin(admin.ModelAdmin):
    list_display = ('analysis_date', 'total_sites', 'region_with_most_sites', 'sites_in_top_region')
    list_filter = ('analysis_date',)

admin.site.register(GalamsaySite, GalamsaySiteAdmin)
admin.site.register(GalamsayAnalysis, GalamsayAnalysisAdmin)