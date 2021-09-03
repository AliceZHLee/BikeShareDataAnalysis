import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']
DAYS=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
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
        try:  
            city=input('Please specify the city to analyze: ')
            city=city.lower()
            if city in CITY_DATA.keys():
                break
            else:
                print('Invalid input')
        except:
            print('Invalid input')
        
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month=input("Please specify the month(january,february,...june) to filter by or just input 'all' to apply no month filter: ")       
            month=month.lower()
            if month=='all' or month in MONTHS:
                break
            else:
                print('Invalid input')   
        except:
            print('Invalid input')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True: 
        try:
            day=input("Please specify the day of week(monday,tuesday,...sunday) to filter by or just input 'all' to apply no day filter: ")
            day=day.lower()
            if day=='all' or day in DAYS:
                break
            else:
                print('Invalid input')
        except:
            print('Invalid input')
            
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
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month!='all':       
        month = MONTHS.index(month) + 1
        df=df[df['month']==month]
    if day!='all':
        df=df[df['day_of_week']==day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The most common month is', MONTHS[df['month'].mode()[0]-1].title())

    # TO DO: display the most common day of week
    print('The most common day of week is',df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    df['Start Hour']=df['Start Time'].dt.hour
    print('The most common start hour is',df['Start Hour'].mode()[0],"o'clock")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used start station is '"+df['Start Station'].mode()[0]+"'")

    # TO DO: display most commonly used end station
    print("The most commonly used end station is '"+df['End Station'].mode()[0]+"'")
    

    # TO DO: display most frequent combination of start station and end station trip
    df['Station Trip']="from '"+df['Start Station']+"' to '"+df['End Station']+"'"
    print('The most frequent combination of start station and end station trip is '+df['Station Trip'].mode()[0])
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time is ', df['Trip Duration'].sum()/3600, ' hours')

    # TO DO: display mean travel time
    print('Mean travel time is ', df['Trip Duration'].mean()/60, ' minutes')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts for different user types:')
    print(df['User Type'].value_counts())
    print()
    # TO DO: Display counts of gender
    print('Counts for gender:')
    if 'Gender' in df.columns:
        print(df['Gender'].value_counts())
    else:
        print("Your input city does not have 'Gender' data for analysis")
       
    # TO DO: Display earliest, most recent, and most common year of birth
    print() 
    print("Analysis for user's birth year")
    if 'Birth Year' in df.columns:
        print('For users, the earliest year of birth is ', int(df['Birth Year'].min()))
        print('For users, the most recent year of birth is ', int(df['Birth Year'].max()))
        print('For users, the most common year of birth is ', int(df['Birth Year'].mode()[0]))        
    else:
        print("Your input city does not have 'year of birth' data for analysis")
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        current_row=0
        rows=df.shape[0]
        while current_row<rows:
            load_raw_data=input('\nwould you like to see 5 lines of raw data? Enter yes or no.\n')                    
            try:
                if load_raw_data.lower()=='yes':        
                    if current_row+5<=rows:
                        print(df[current_row:(current_row+5)])
                        current_row+=5
                        continue
                    else:
                        print(df[current_row:rows])                
                        print('\nThere is no more data to display')
                        break  
                elif load_raw_data.lower()=='no':
                    break
                else:
                    print('Invalid Input')
            except:
                print('Invalid input')
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
