"""
EIA Data Fetcher for Gasoline Trading Analysis
This script fetches gasoline and crude oil price data from the EIA API
"""

import requests
import pandas as pd
import json
from datetime import datetime, timedelta
import os

class EIADataFetcher:
    """
    Fetches energy price data from the U.S. Energy Information Administration (EIA) API
    """
    
    def __init__(self, api_key=None):
        """
        Initialize the EIA data fetcher
        
        Args:
            api_key (str): Your EIA API key. Get one free at https://www.eia.gov/opendata/
        """
        self.api_key = api_key or self._get_api_key_from_config()
        self.base_url = "https://api.eia.gov/v2/petroleum/pri/spt/data/"
        
        if not self.api_key:
            raise ValueError("EIA API key is required. Get one free at https://www.eia.gov/opendata/")
    
    def _get_api_key_from_config(self):
        """Try to load API key from config file"""
        try:
            # This will work when we set up the config file
            import yaml
            with open('config/config.yaml', 'r') as file:
                config = yaml.safe_load(file)
                return config['api_keys']['eia_api_key']
        except:
            return None
    
    def fetch_gasoline_prices(self, start_date="2023-01-01", end_date=None):
        """
        Fetch weekly gasoline prices from EIA
        
        Args:
            start_date (str): Start date in YYYY-MM-DD format
            end_date (str): End date in YYYY-MM-DD format (defaults to today)
            
        Returns:
            pandas.DataFrame: DataFrame with dates and gasoline prices
        """
        if end_date is None:
            end_date = datetime.now().strftime("%Y-%m-%d")
        
        # EIA series ID for weekly gasoline prices (dollars per gallon)
        series_id = "PET.EER_EPMRR_PF4_RGC_DPG.W"
        
        url = f"https://api.eia.gov/v2/petroleum/pri/gnd/data/"
        
        params = {
            'api_key': self.api_key,
            'frequency': 'weekly',
            'data[0]': 'value',
            'facets[series][]': series_id,
            'start': start_date,
            'end': end_date,
            'sort[0][column]': 'period',
            'sort[0][direction]': 'desc',
            'offset': 0,
            'length': 5000
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            
            data = response.json()
            
            if 'data' in data and data['data']:
                df = pd.DataFrame(data['data'])
                df['date'] = pd.to_datetime(df['period'])
                df['gasoline_price'] = pd.to_numeric(df['value'])
                df = df[['date', 'gasoline_price']].sort_values('date')
                
                print(f"✅ Successfully fetched {len(df)} gasoline price records")
                return df
            else:
                print("❌ No gasoline data found")
                return pd.DataFrame()
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Error fetching gasoline data: {e}")
            return pd.DataFrame()
        except Exception as e:
            print(f"❌ Error processing gasoline data: {e}")
            return pd.DataFrame()
    
    def fetch_crude_oil_prices(self, start_date="2023-01-01", end_date=None):
        """
        Fetch weekly crude oil prices from EIA
        
        Args:
            start_date (str): Start date in YYYY-MM-DD format
            end_date (str): End date in YYYY-MM-DD format (defaults to today)
            
        Returns:
            pandas.DataFrame: DataFrame with dates and crude oil prices
        """
        if end_date is None:
            end_date = datetime.now().strftime("%Y-%m-%d")
        
        # EIA series ID for WTI crude oil spot prices
        series_id = "PET.RWTC.W"
        
        url = f"https://api.eia.gov/v2/petroleum/pri/spt/data/"
        
        params = {
            'api_key': self.api_key,
            'frequency': 'weekly',
            'data[0]': 'value',
            'facets[series][]': series_id,
            'start': start_date,
            'end': end_date,
            'sort[0][column]': 'period',
            'sort[0][direction]': 'desc',
            'offset': 0,
            'length': 5000
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            
            data = response.json()
            
            if 'data' in data and data['data']:
                df = pd.DataFrame(data['data'])
                df['date'] = pd.to_datetime(df['period'])
                df['crude_price'] = pd.to_numeric(df['value'])
                df = df[['date', 'crude_price']].sort_values('date')
                
                print(f"✅ Successfully fetched {len(df)} crude oil price records")
                return df
            else:
                print("❌ No crude oil data found")
                return pd.DataFrame()
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Error fetching crude oil data: {e}")
            return pd.DataFrame()
        except Exception as e:
            print(f"❌ Error processing crude oil data: {e}")
            return pd.DataFrame()
    
    def test_connection(self):
        """
        Test if the API connection is working
        
        Returns:
            bool: True if connection successful, False otherwise
        """
        try:
            # Simple test request
            url = "https://api.eia.gov/v2/petroleum/pri/spt/data/"
            params = {
                'api_key': self.api_key,
                'frequency': 'weekly',
                'data[0]': 'value',
                'facets[series][]': 'PET.RWTC.W',
                'start': '2024-01-01',
                'end': '2024-01-07',
                'length': 1
            }
            
            response = requests.get(url, params=params, timeout=10)
            
            if response.status_code == 200:
                print("✅ EIA API connection successful!")
                return True
            else:
                print(f"❌ EIA API connection failed. Status code: {response.status_code}")
                return False
                
        except Exception as e:
            print(f"❌ EIA API connection failed: {e}")
            return False

# Simple test function
def test_eia_fetcher():
    """Test the EIA data fetcher with your API key"""
    
    # You'll need to replace this with your actual API key for testing
    api_key = "YOUR_API_KEY_HERE"  # Replace with your actual key
    
    print("🧪 Testing EIA Data Fetcher...")
    print("=" * 50)
    
    try:
        # Initialize fetcher
        fetcher = EIADataFetcher(api_key=api_key)
        
        # Test connection
        if not fetcher.test_connection():
            print("❌ Cannot connect to EIA API. Check your API key.")
            return
        
        # Fetch recent data
        print("\n📈 Fetching recent gasoline prices...")
        gas_data = fetcher.fetch_gasoline_prices(start_date="2024-01-01")
        
        print("\n🛢️ Fetching recent crude oil prices...")
        crude_data = fetcher.fetch_crude_oil_prices(start_date="2024-01-01")
        
        if not gas_data.empty and not crude_data.empty:
            print("\n🎉 Success! Here's a sample of your data:")
            print("\nGasoline Prices (last 5 records):")
            print(gas_data.tail())
            
            print("\nCrude Oil Prices (last 5 records):")
            print(crude_data.tail())
            
            print(f"\n📊 Data Summary:")
            print(f"   • Gasoline records: {len(gas_data)}")
            print(f"   • Crude oil records: {len(crude_data)}")
            print(f"   • Date range: {gas_data['date'].min().date()} to {gas_data['date'].max().date()}")
        
    except Exception as e:
        print(f"❌ Test failed: {e}")

if __name__ == "__main__":
    # Run test when script is executed directly
    test_eia_fetcher()