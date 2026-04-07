# Quarterly-PM2.5-FRM-FEM-Comparisons
My first project on Github. Our database does not have a good way for comparison of continuous and filter based air monitoring samples. Instead of pasting our PM2.5 into excel each quarter, I tried my hand at automating things. 

This script visualizes air quality PM2.5 concentrations from the Cannons Lane monitoring site, generating quarterly plots for 2025. All data were retrieved from EPA's Air Quality System (AQS) database.

## Overview

This script processes air quality monitoring data and creates time-series visualizations of Daily Mean PM2.5 Concentration levels, broken down by measurement method for each quarter of 2025. It's useful for environmental monitoring, air quality analysis, and tracking seasonal patterns.

## Features

- **CSV Data Processing**: Reads air quality monitoring data from a CSV file
- **Site Filtering**: Extracts data specifically for the CANNONS LANE location
- **Quarterly Analysis**: Automatically divides data into four quarters (Q1-Q4 2025)
- **Multi-Method Visualization**: Plots separate lines for each measurement method
- **High-Resolution Output**: Saves plots as 300 DPI PNG files
- **Comprehensive Display**: Shows all rows and columns of the dataset for better visibility

## Requirements

- Python 3.6+
- pandas
- matplotlib

## Installation

1. Clone or download this repository
2. Install the required dependencies:
```bash
pip install pandas matplotlib
```

## Usage

1. Prepare your data file named `ad_viz_plotval_data.csv` in the same directory as the script. The CSV must contain the following columns:
   - `Local Site Name` - Location identifier
   - `Date` - Measurement date
   - `Method Description` - Type/method of measurement
   - `Daily Mean PM2.5 Concentration` - PM2.5 concentration value

2. Run the script:
```bash
python sample.py
```

3. The script will generate four PNG files:
   - `cannons_lane_plot_Q1.png` - January to March 2025
   - `cannons_lane_plot_Q2.png` - April to June 2025
   - `cannons_lane_plot_Q3.png` - July to September 2025
   - `cannons_lane_plot_Q4.png` - October to December 2025

## Output

Each generated plot includes:
- Time-series line plots showing PM2.5 concentration trends
- Separate lines for each measurement method
- Grid lines for easier reading
- Legend identifying each method
- High-resolution format suitable for reports and presentations

## Example CSV Format

```
Local Site Name,Date,Method Description,Daily Mean PM2.5 Concentration
CANNONS LANE,2025-01-01,Method A,15.3
CANNONS LANE,2025-01-02,Method A,14.8
CANNONS LANE,2025-01-02,Method B,15.1
```

## Customization

You can modify the script to:
- Change the target site: Update `'CANNONS LANE'` in the filtering line
- Adjust plot dimensions: Modify `figsize=(14,6)` parameter
- Change DPI: Adjust `dpi=300` in the `savefig()` call
- Modify quarters: Edit the `quarters` list for different date ranges

## Notes

- The script uses TkAgg backend for matplotlib rendering
- All rows and columns from the dataframe are displayed in the console output
- Ensure your CSV data is clean and contains valid dates for proper processing
