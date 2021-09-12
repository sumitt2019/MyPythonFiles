import pandas as pd
import datetime

input_file = r'C:\Users\username\file_folder\input_file.csv'
raw_data = pd.read_csv(input_file,  error_bad_lines=False)


#condition is to filter only the columns with date greater than the some selected date

datetime.datetime.strptime
raw_data['date_column']= pd.to_datetime(raw_data['date_column'])                            #converting the date column into date format
filtered_data = raw_data[(raw_data['date_column'] > datetime.date(2021,1,1) )]              #filtering the date column based on user filter

output_file = r'C:\Users\username\file_folder\outut_file.csv'
filtered_data.to_csv(output_file)
