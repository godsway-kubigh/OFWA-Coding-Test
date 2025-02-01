from rest_framework import viewsets
from .models import GalamsaySite, GalamsayAnalysis
from .serializers import GalamsaySiteSerializer, GalamsayAnalysisSerializer


class GalamsaySiteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GalamsaySite.objects.all()
    serializer_class = GalamsaySiteSerializer
    
    def get_queryset(self):
        queryset = GalamsaySite.objects.all()
        region = self.request.query_params.get('region', None)
        if region:
            queryset = queryset.filter(region=region)
        return queryset

class GalamsayAnalysisViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GalamsayAnalysis.objects.order_by('-analysis_date')
    serializer_class = GalamsayAnalysisSerializer