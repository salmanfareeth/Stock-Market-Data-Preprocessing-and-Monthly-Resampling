import pandas as pd
import os

welcome_art = r"""
   _____                _ _        _____                    _            
  / ____|              | ( )      / ____|                  | |           
 | (___  _   _  ___  __| |/ ___  | |     _____   _____ _ __| |_ ___ _ __ 
  \___ \| | | |/ _ \/ _` | / __| | |    / _ \ \ / / _ \ '__| __/ _ \ '__|
  ____) | |_| |  __/ (_| | \__ \ | |___| (_) \ V /  __/ |  | ||  __/ |   
 |_____/ \__, |\___|\__,_| |___/  \_____\___/ \_/ \___|_|   \__\___|_|   
          __/ |                                                          
         |___/                                                           
"""

print(welcome_art)

# Load the data or file
file_path = '/data_path/'  
data = pd.read_csv(file_path)

# Preprocessing
# Convert 'Date' column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Remove '$' and convert price columns to numeric
price_columns = ['Close/Last', 'Open', 'High', 'Low']
for col in price_columns:
    data[col] = data[col].replace({r'\$': ''}, regex=True).astype(float)

# Resample data to monthly frequency
monthly_data = data.set_index('Date').resample('ME').agg({
    'Close/Last': 'last',  # Last closing price of the month
    'Volume': 'sum',       # Total volume traded in the month
    'Open': 'first',       # Opening price of the first trading day of the month
    'High': 'max',         # Maximum price in the month
    'Low': 'min'           # Minimum price in the month
}).reset_index()


output_path = '/Output_path/' 

# Ensure the directory exists
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Save the monthly data to a CSV file
monthly_data.to_csv(output_path, index=False)

print(f"Monthly data has been saved to {output_path}")