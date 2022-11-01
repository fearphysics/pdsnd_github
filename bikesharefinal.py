import time
from datetime import datetime
import pandas as pd
import numpy as np
import glob
import os

# 
"""cities = ('./')
file_list = os.listdir(cities)

file_list = glob.glob('*.{}'.format('csv'))

print(file_list)"""


cities = ('./')
file_list = os.listdir(cities)

file_list = glob.glob('*.{}'.format('csv'))
df_append = pd.DataFrame()
for file in file_list:
    
    df_temp = pd.read_csv(file)
    df_temp['city'] = file[:-4]
    df_append = df_append.append(df_temp, ignore_index=True)

df_append['Start Time'] = pd.to_datetime(df_append['Start Time'], format='%Y-%m-%d %H:%M')

print('Hello! Let\'s explore some US bikeshare data!\n')


CITY_DATA = { 'chicago': 'chicago',
              'new york city': 'new_york_city',
              'washington': 'washington' }

available_cities = df_append['city'].unique()
  

print('These are the available cities\n')
print(list(CITY_DATA.keys()))
print('\n Select city from list above: Enter exactly as shown\n')



city = None
while city not in CITY_DATA.keys():
    print('\n')
    city = str(input("Enter city:"))
    print('-'*40)
if  city in CITY_DATA.keys():
    city_df = df_append[df_append['city'] == CITY_DATA[city]]
    


df_append['month'] = df_append['Start Time'].dt.month_name()
available_months = df_append['month'].unique()
available_months = np.append(available_months, 'all')
df_append['day'] = df_append['Start Time'].dt.day_name()
month = None
print(available_months)
print('\nSelect Month from list above:Enter exactly as shown')
while month not in available_months:
    print('\n')
    month = str(input("\nEnter Month:"))
    print('-'*40)
    if  month not in available_months:
        print('Check list of of availble months: Enter exactly as shown')
    
if  month in available_months:
    if month == 'all':
        month_df = df_append.copy()
    else:
        month_df = df_append[df_append['month'] == month]
    

available_days = df_append['day'].unique()
available_days = np.append(available_days, 'all')

day = None
print(available_days)
print('\nPlease select Day from the available days above: Enter exactly as shown')
while day not in available_days:
    print('\n')
    day = str(input("\nEnter Day:"))
    print('-'*40)
    if  day not in available_days:
        print('Check list of of availble days: Enter exactly as shown')
if  day in available_days:
    if day == 'all':
        day_df = month_df.copy()
    else:
        day_df = month_df[month_df['day'] == day]
        
print('\n')
start_time = time.time()
print("\nThis took %s seconds." % (time.time() - start_time))
print('\nUser Selections')
print(city, month, day)
print('-'*40)

# df_subset = df_append[(df_append['city'] == city) & (df_append['month'] == month) & (df_append['day'] == day)]
df_subset = day_df.copy()
"""print(df_subset.head())"""

"""-----------------------Stats------------------------------"""
print('\nCalculating The Most Frequent Times of Travel...\n')


print('\nMost Popular Month')
most_popular_month = df_append['month'].mode()[0]
print(most_popular_month)

print('\nMost Popular Day')
most_popular_day = df_append['day'].mode()[0]
print(most_popular_day)

print('\nMost Popular Hour')
df_subset['hour'] = df_subset['Start Time'].dt.hour
most_popular_hour = df_subset['hour'].mode()[0]
print(most_popular_hour)
"""-------------------------------------------------------------------"""
print('-'*40)
print('\nCalculating The Most Popular Stations and Trip...\n')

print('\nMost Common Starting Station')
most_common_start_station = df_subset['Start Station'].mode()[0]
print(most_common_start_station)

print('\nMost Common Ending Station')
most_common_end_station = df_subset['End Station'].mode()[0]
print(most_common_end_station)

print('\nMost Common Start And End Stations')
df_subset['Start and End'] = df_subset['Start Station'].str.cat(df_subset['End Station'], sep=' to ')
Start_and_End = df_subset['Start and End'].mode()[0]

most_common_start_to_end_station = df_subset['Start and End'].mode()[0]
print(most_common_start_to_end_station)
"""--------------------------------------------------------------------"""
print('-'*40)
print('\nCalculating Trip Duration...\n')
    
trip_times_sec = df_subset['Trip Duration'].sum()
trip_times_hour = trip_times_sec / 3600
minutes = round((trip_times_hour * 60) % 60,3)
seconds = round((minutes * 60) % 60,3)

print('\nSum of Trip Durations')
print("%d:%02d:%02d" % (trip_times_hour, minutes, seconds))

print('\nAverage Trip Duration')
avg_duration_sec = np.average(df_subset['Trip Duration'])
avg_hour = avg_duration_sec / 3600
avg_min = round((avg_hour * 60) % 60,2)
avg_sec = round((avg_min * 60) % 60, 1)
print(str(int(avg_min))  + " " + "Minutes",str(int(avg_sec))   + " " + "Seconds")

"""---------------------------------------------------------------------"""
df_subset = df_subset.rename(columns = {'Unnamed: 0' : 'ID'})
print('-'*40)
print('\nCalculating User Stats...\n')
user_type = df_append['User Type'].unique()
user_type_count = df_subset.groupby('User Type')['ID'].count()

print(user_type_count,'\n')
"""user_type_count.to_csv('count.csv')"""

user_gender = df_append['Gender'].unique()
user_type_gender = df_subset.groupby('Gender')['ID'].count()

print(user_type_gender,'\n')
print('-'*40)
print('Birth Years\n')
earliest = int(df_subset['Birth Year'].min())
print('Earliest')
print(earliest,'\n')
most_recent = int(df_subset['Birth Year'].max())
print('Most Recent')
print(most_recent,'\n')
most_common_year = int(df_subset['Birth Year'].mode()[0])
print('Most Common')
print(most_common_year,'\n')