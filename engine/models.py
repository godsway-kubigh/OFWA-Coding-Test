from django.db import models


class GalamsaySite(models.Model):
    """
    Database for Galamsay mining sites
    """
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    number_of_sites = models.IntegerField()
    
    class Meta:
        unique_together = ('city', 'region')
        verbose_name_plural = "Galamsay Sites"
    
    def __str__(self):
        return f"{self.city}, {self.region}: {self.number_of_sites} sites"


class GalamsayAnalysis(models.Model):
    """
    Database for analysis results of galamsay sites data
    """
    total_sites = models.IntegerField()
    region_with_most_sites = models.CharField(max_length=100)
    sites_in_top_region = models.IntegerField()
    analysis_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Analysis on {self.analysis_date}"