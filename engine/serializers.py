from rest_framework import serializers
from .models import GalamsaySite, GalamsayAnalysis

class GalamsaySiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalamsaySite
        fields = ['id', 'city', 'region', 'number_of_sites']

class GalamsayAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalamsayAnalysis
        fields = ['id', 'total_sites', 'region_with_most_sites', 'sites_in_top_region', 'analysis_date']