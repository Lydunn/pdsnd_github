import time
import pandas as pd
import numpy as np
#only months that will have data available
Months = ['january', 'february', 'march', 'april', 'may', 'june']
Days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
   # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("\nWhich of the following cities would you like to see data for Chicago, New York City or Washington?\n").lower()
        if city.lower() not in CITY_DATA:
           print("Please enter a city listed above:")
        else:
           break
        
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("\nPlease pick a month that you would like data on between January-June?\n").lower()
        if month.lower() not in Months:
           print("Please enter a month between January-June:")
        else:
           break
                  
      # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input("\nPlease pick a day of week that you would like data for.\n")
        if day.lower() not in Days:
          print ("Please chose a day between Sunday-Saturday")
        else:
           break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("Most common month:", common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("Most common day:", common_day)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour=df['hour'].mode()[0]
    print("Most common start hour:", common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print(df.head())
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    common_start = df['Start Station'].mode()[0]
    print("Most commonly used start station:", common_start)
    
    # TO DO: display most commonly used end station

    end_station = df['End Station'].mode()[0]
    print("Most commonly used end station:", end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combination_station = df[['Start Station', 'End Station']]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total Travel Time:", total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean Travel Time:", mean_travel_time)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    

    # TO DO: Display counts of gender
    if 'Gender' in (df.columns):
        print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in (df.columns):
        earliest_year_of_birth = int(df['Birth Year'].min())
        print("The earliest year of birth is:", earliest_year_of_birth)
        most_recent_year_of_birth = int(df['Birth Year'].max())
        print("The most recent of year of birth:", most_recent_year_of_birth,)
        most_common_year_of_birth = int(df['Birth Year'].mode()[0])
        print("The most common year of birth is:", most_common_year_of_birth)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
   #If user wants 5 rows of raw data#
    raw_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()
    start_loc = 0
    while True:
        print(df.iloc[start_loc: start_loc+5])
        start_loc += 5
        view_display = input("Do you wish to continue?: ").lower()
        break
    

def main():
  
   while True:
       city, month, day = get_filters()
       df = load_data(city, month, day)

       time_stats(df)
       station_stats(df)
       trip_duration_stats(df)
       user_stats(df)
       raw_data(df) 

       restart = input('\nWould you like to restart? Enter yes or no.\n')
       if restart.lower() != 'yes':
           break
if __name__ == "__main__":
    main()
