import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months_1 = ('january', 'february', 'march', 'april', 'may', 'june', 'all')
days_1 = ('monday', 'tuesday', 'wendesday', 'thursday', 'friday', 'saturday', 'sunday', 'all')

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        city = input("What city do you want to filter by? Choose from the following: Chicago, New York City, or Washington.\n").lower()
        if city not in CITY_DATA:
            print("Kindly make sure you chose one of the three cities and that you used the correct spelling.\n")
            continue
        else:
            break
""" this part of the function takes input from the user to filter by city"""
    while True:
        month = input("What month do you to filter by? January, February, March, April, May, or June? If none, please type 'all'.\n").lower()
        if month not in months_1:
            print("Kindly make sure you either selected one of the six months or type 'all' and are using the correct spelling")
            continue
        else:
            break
""" this part of the function takes input from the user to filter by month """
    while True:
        day = input("Which day do you want to filter by? Monday, Tuesday, Wednesday, etc. If none, please type 'all'.\n")
        if day not in days_1:
            print("Kindly make sure your spelling is correct!\n")
            continue
        else:
            break
""" this part of the function takes input from the user to filter by month """

    """
    the function defined above asks user to specify a city, month, and day to analyze.
    It returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Refer to documentation below each part of the function for the specific purpose
    of the part
    """
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    # get user input for month (all, january, february, ... , june)


    # get user input for day of week (all, monday, tuesday, ... sunday)


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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()[0]
    print(most_common_month)


    # display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print(most_common_day)


    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print(most_common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start = df['Start Station'].mode()[0]
    print(most_common_start)


    # display most commonly used end station
    most_common_end = df['End Station'].mode()[0]
    print(most_common_end)


    # display most frequent combination of start station and end station trip
    df['station_combination'] = df['Start Station'] + "and" + df['End Station']
    most_common_combination = df['station_combination'].mode()[0]
    print(most_common_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(total_travel_time)


    # display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print(average_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types_counts = df['User Type'].value_counts()
    print(user_types_counts)


    # Display counts of gender
    if 'Gender' in df:
        gender_counts = df['Gender'].value_counts()
        print(gender_counts)
    else:
        print("We don't have any gender data for this city.")


    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth_year = df['Birth Year'].min()
        print(earliest_birth_year)
        most_recent_birth_year = df['Birth Year'].max()
        print(most_recent_birth_year)
        most_common_birth_year = df['Birth Year'].mode()[0]
        print(most_common_birth_year)
    else:
        print("We don't have any data regarding the birth years of our users.")



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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
