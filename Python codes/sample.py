import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

pd.set_option('display.max_rows', None) #displays all rows of the dataframe.
pd.set_option('display.max_columns', None) #displays all columns of the dataframe.

df = pd.read_csv('ad_viz_plotval_data.csv')

#Filter for Cannons Lane
cannons_lane = df[df['Local Site Name'] == 'CANNONS LANE'] #adjust column name if needed

#Convert data column to datetime (adjust column name if needed)
cannons_lane['Date'] = pd.to_datetime(cannons_lane['Date'])

#Define quarters
quarters = [
    ('Q1 (Jan-Mar 2025)', '2025-01-01', '2025-03-31'),
    ('Q2 (Apr-Jun 2025)', '2025-04-01', '2025-06-30'),
    ('Q3 (Jul-Sep 2025)', '2025-07-01', '2025-09-30'),
    ('Q4 (Oct-Dec 2025)', '2025-10-01', '2025-12-31')
]

#Create a plot for each quarter
for quarter_name, start_date, end_date in quarters:
    quarter_data = cannons_lane[(cannons_lane['Date'] >= start_date) & (cannons_lane['Date'] <= end_date)]
    
    plt.figure(figsize=(14,6))
    
    #Plot each method designation separately
    for method in quarter_data['Method Description'].unique():
        data = quarter_data[quarter_data['Method Description'] == method]
        data = data.sort_values('Date')
        plt.plot(data['Date'], data['Daily Mean PM2.5 Concentration'], label=method)
    
    plt.xlabel('Date')
    plt.ylabel('Daily Mean PM2.5 Concentration')
    plt.title(f'Cannons Lane Daily Mean PM2.5 by Method Designation - {quarter_name}')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    #Save with quarter-specific filename
    filename = f"cannons_lane_plot_{quarter_name.split()[0]}.png"
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"Plot saved as '{filename}'")
    plt.close()

print("All quarterly plots saved!")