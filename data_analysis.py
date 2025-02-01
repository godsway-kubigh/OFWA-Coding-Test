import pandas as pd
import csv
from typing import Dict, List, Tuple


def load_data(file_path: str) -> pd.DataFrame:
    """
    Load Galamsay data from xlsx file.
    
    Args:
        file_path (str): Path to the xlsx file
    
    Returns:
        pd.DataFrame: Loaded dataframe
    """

    try:
        # Remove duplicate rows and handle invalid entries
        df = pd.read_excel(file_path)
        # Convert Number_of_Galamsay_Sites to numeric, invalid values become NaN
        df['Number_of_Galamsay_Sites'] = pd.to_numeric(df['Number_of_Galamsay_Sites'], errors='coerce')
        print(df)
        return df
    
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return pd.DataFrame()
    
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()

def calculate_total_sites(df: pd.DataFrame) -> int:
    """
    Calculate total number of Galamsay sites across all cities.
    
    Args:
        df (pd.DataFrame): Input dataframe
    
    Returns:
        int: Total number of Galamsay sites
    """
    return int(df['Number_of_Galamsay_Sites'].sum())

def find_region_with_most_sites(df: pd.DataFrame) -> Tuple[str, int]:
    """
    Find the region with the highest number of Galamsay sites.
    
    Args:
        df (pd.DataFrame): Input dataframe
    
    Returns:
        Tuple[str, int]: Region name and number of sites
    """
    region_sites = df.groupby('Region')['Number_of_Galamsay_Sites'].sum()
    return region_sites.idxmax(), region_sites.max()

def list_cities_above_threshold(df: pd.DataFrame, threshold: int = 10) -> List[Dict[str, int]]:
    """
    List cities with Galamsay sites exceeding a given threshold.
    
    Args:
        df (pd.DataFrame): Input dataframe
        threshold (int, optional): Minimum number of sites. Defaults to 10.
    
    Returns:
        List[Dict[str, int]]: List of cities and their site counts
    """
    cities_above_threshold = df[df['Number_of_Galamsay_Sites'] > threshold]
    return cities_above_threshold[['City', 'Number_of_Galamsay_Sites']].to_dict('records')

def calculate_average_sites_per_region(df: pd.DataFrame) -> Dict[str, float]:
    """
    Calculate average number of Galamsay sites per region.
    
    Args:
        df (pd.DataFrame): Input dataframe
    
    Returns:
        Dict[str, float]: Region-wise average sites
    """
    return df.groupby('Region')['Number_of_Galamsay_Sites'].mean().to_dict()

def analyze_galamsay_data(file_path: str) -> Dict:
    """
    Comprehensive analysis of Galamsay data.
    
    Args:
        file_path (str): Path to the CSV file
    
    Returns:
        Dict: Analysis results
    """
    # Load data
    df = load_data('data/galamsay_data.xlsx')
    
    if df.empty:
        return {"error": "No valid data found"}
    
    # Perform analyses
    return {
        "total_sites": calculate_total_sites(df),
        "region_with_most_sites": find_region_with_most_sites(df),
        "cities_above_threshold": list_cities_above_threshold(df),
        "average_sites_per_region": calculate_average_sites_per_region(df)
    }

# Example usage
if __name__ == "__main__":
    results = analyze_galamsay_data('data/galamsay_data.xlsx')
    print(results)