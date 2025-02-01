import os
import django
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "root.settings")
django.setup()

from engine.models import GalamsaySite, GalamsayAnalysis
from data_analysis import analyze_galamsay_data

def upload_galamsay_data(file_path):
    df = pd.read_excel(file_path)
    
    # Convert to numeric and clean data
    df['Number_of_Galamsay_Sites'] = pd.to_numeric(df['Number_of_Galamsay_Sites'], errors='coerce')
    df = df.dropna(subset=['Number_of_Galamsay_Sites'])
    df = df[df['Number_of_Galamsay_Sites'] >= 0]
    df = df.drop_duplicates()
    
    sites_to_create = []
    for _, row in df.iterrows():
        site, created = GalamsaySite.objects.update_or_create(
            city=row['City'],
            region=row['Region'],
            defaults={'number_of_sites': int(row['Number_of_Galamsay_Sites'])}
        )
        sites_to_create.append(site)
    
    analysis_results = analyze_galamsay_data(file_path)
    
    GalamsayAnalysis.objects.create(
        total_sites=analysis_results['total_sites'],
        region_with_most_sites=analysis_results['region_with_most_sites'][0],
        sites_in_top_region=analysis_results['region_with_most_sites'][1]
    )
    
    print(f"Uploaded {len(sites_to_create)} Galamsay sites")

if __name__ == "__main__":
    upload_galamsay_data('data/galamsay_data.xlsx')