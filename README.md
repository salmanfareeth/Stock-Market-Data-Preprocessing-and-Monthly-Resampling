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

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/salmanfareeth/Stock-Market-Data-Preprocessing-and-Monthly-Resampling.git
    cd Stock-Market-Data-Preprocessing-and-Monthly-Resampling
    ```

## References

- [Pandas Documentation](https://pandas.pydata.org/docs/) - For data manipulation and analysis.
- [Python OS Module](https://docs.python.org/3/library/os.html) - For interacting with the operating system.
- [Datetime Module](https://docs.python.org/3/library/datetime.html) - For working with dates and times.
- [CSV File Format](https://en.wikipedia.org/wiki/Comma-separated_values) - Explanation of CSV file structure and usage.
- [Pandas Resample Method](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.resample.html) - Detailed documentation on data resampling.
- [Python Regex (Regular Expressions)](https://docs.python.org/3/library/re.html) - For replacing strings using patterns.


## Developer Note

Script developed and maintained by `salmanfareeth`.
This tool is in beta version.
