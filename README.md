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

## Dependencies

**Python 3.7 or higher**

## Required libraries

### Install the dependencies using pip

```py
pip install pandas
pip install os
```


bash
Copy code
pip install pandas
