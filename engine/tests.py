import pytest
import pandas as pd
from django.test import TestCase
from engine.models import GalamsaySite, GalamsayAnalysis
from data_analysis import (
    load_data, 
    calculate_total_sites, 
    find_region_with_most_sites, 
    list_cities_above_threshold,
    calculate_average_sites_per_region
)
from upload_data import upload_galamsay_data

@pytest.mark.django_db
class TestGalamsayAnalysis:
    def test_load_data(self, tmp_path):
        # Create a test CSV file
        test_data = pd.DataFrame({
            'City': ['Accra', 'Kumasi'],
            'Region': ['Greater Accra', 'Ashanti'],
            'Number_of_Galamsay_Sites': [30, 25]
        })
        test_file = tmp_path / "test_data.csv"
        test_data.to_csv(test_file, index=False)
        
        # Test data loading
        df = load_data(test_file)
        assert len(df) == 2
        assert df['Number_of_Galamsay_Sites'].sum() == 55
    
    def test_total_sites(self, tmp_path):
        test_data = pd.DataFrame({
            'City': ['Accra', 'Kumasi'],
            'Region': ['Greater Accra', 'Ashanti'],
            'Number_of_Galamsay_Sites': [30, 25]
        })
        test_file = tmp_path / "test_data.csv"
        test_data.to_csv(test_file, index=False)
        
        df = load_data(test_file)
        total = calculate_total_sites(df)
        assert total == 55
    
    def test_region_with_most_sites(self, tmp_path):
        test_data = pd.DataFrame({
            'City': ['Accra', 'Kumasi', 'Takoradi'],
            'Region': ['Greater Accra', 'Ashanti', 'Western'],
            'Number_of_Galamsay_Sites': [30, 25, 18]
        })
        test_file = tmp_path / "test_data.csv"
        test_data.to_csv(test_file, index=False)
        
        df = load_data(test_file)
        top_region, sites = find_region_with_most_sites(df)
        assert top_region == 'Greater Accra'
        assert sites == 30
    
    def test_upload_data(self, tmp_path):
        test_data = pd.DataFrame({
            'City': ['Accra', 'Kumasi'],
            'Region': ['Greater Accra', 'Ashanti'],
            'Number_of_Galamsay_Sites': [30, 25]
        })
        test_file = tmp_path / "test_data.csv"
        test_data.to_csv(test_file, index=False)
        
        upload_galamsay_data(test_file)
        
        assert GalamsaySite.objects.count() == 2
        assert GalamsayAnalysis.objects.count() == 1