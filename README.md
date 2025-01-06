# 📊 Stock Market Data Preprocessing and Monthly Resampling 🗓️
# Data Preprocessing and Resampling Script

This Python script processes a CSV file containing stock market data, performs data cleaning and preprocessing, and resamples the data to a monthly frequency. The processed data is then saved as a CSV file for further analysis.

## Features

- Converts date strings to `datetime` format.
- Removes dollar signs (`$`) and converts price columns to numeric types.
- Aggregates data to a monthly frequency with specific metrics:
  - **Close/Last**: Last closing price of the month.
  - **Volume**: Total volume traded in the month.
  - **Open**: Opening price of the first trading day of the month.
  - **High**: Maximum price during the month.
  - **Low**: Minimum price during the month.
- Saves the processed data to a specified output directory.

## Welcome Art

```plaintext
   _____                _ _        _____                    _            
  / ____|              | ( )      / ____|                  | |           
 | (___  _   _  ___  __| |/ ___  | |     _____   _____ _ __| |_ ___ _ __ 
  \___ \| | | |/ _ \/ _` | / __| | |    / _ \ \ / / _ \ '__| __/ _ \ '__|
  ____) | |_| |  __/ (_| | \__ \ | |___| (_) \ V /  __/ |  | ||  __/ |   
 |_____/ \__, |\___|\__,_| |___/  \_____\___/ \_/ \___|_|   \__\___|_|   
          __/ |                                                          
         |___/                                                           
