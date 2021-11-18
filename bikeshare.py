"""
Udacity Bikeshare Project
This Python script is written for as part of requirement for the second project of the Programming for Data Science with Python Nanodegree Program and is used to explore data related to Bikeshare in Chicago, New York City, and Washington cities. It imports data from csv files and compute descriptive statistics from the data. It also takes in users' raw input to create an interactive experience in the terminal to present these statistics.

The following were the pages I referred to in completing the project:

https://knowledge.udacity.com/questions/723852
https://knowledge.udacity.com/questions/723923
https://knowledge.udacity.com/questions/721865
https://stackoverflow.com/questions/19377969/combine-two-columns-of-text-in-dataframe-in-pandas-python
https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
https://github.com/Aritra96/bikeshare-project/blob/master/bikeshare.py
https://stackoverflow.com/questions/2847386/python-string-and-integer-concatenation
https://stackoverflow.com/questions/4183506/python-list-sort-in-descending-order
https://www.geeksforgeeks.org/python-pandas-series-dt-month/
https://stackoverflow.com/questions/51684178/i-am-getting-a-syntax-error-return-outside-function


"""




import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_DATA = ["january", "february", "march", "april", "may", "june", "all"]
DAY_DATA = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "all"]
              

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
    name_of_city = ""
    while name_of_city.lower() not in CITY_DATA:
        name_of_city = input("What city would you like to see data for... Is it Chicago, New York city or Washington?")
        if name_of_city.lower() in CITY_DATA:
            city  = CITY_DATA[name_of_city.lower()]
        else:
            print("Apologies, kindly input the correct city you want in the format i.e. ['Chicago', 'New Your City', 'Washington']")


        # TO DO: get user input for month (all, january, february, ... , june)
    name_of_month = ""
    while name_of_month.lower() not in MONTH_DATA:
        name_of_month = input("What month would you like to see?... Is it January, February, ....June or all the months?")
        if name_of_month.lower() in MONTH_DATA:
            month = name_of_month.lower()
        else:
            print("Apologies, kindly input the correct month i.e. ['january', 'february', 'march', 'april', 'may', 'june', or 'all']")

        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    name_of_day = ""
    while name_of_day.lower() not in DAY_DATA:
        name_of_day = input("What day of the week would you like to see?.... Is it Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or all days?")
        if name_of_day.lower() in DAY_DATA:
            day = name_of_day.lower()
        else:
              print("Apologies, kindly input the correct day i.e. ['sunday', 'monday', 'tuesday', .....saturday or 'all']")

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
    # to load data file into dataframe              
    df = pd.read_csv(city)

    # to change Start Time to datetime              
    df["Start Time"] = pd.to_datetime(df["Start Time"])

     # to create new columns month, day of the week, hour from Start Time
    df["month"] = df["Start Time"].dt.month
    df["name_of_day"] = df["Start Time"].dt.weekday_name
    df["hour"] = df["Start Time"].dt.hour
              

    if month != "all":
        month = MONTH_DATA.index(month)
        df = df.loc[df["month"] == month]
                    
        if day != "all":
            df = df.loc[df["name_of_day"] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df["month"].mode()[0]
    print("The most common month is: " , common_month)

    # TO DO: display the most common day of week
    common_day_of_the_week = df["name_of_day"].mode()[0]
    print("The most common day of week: " , common_day_of_the_week)


    # TO DO: display the most common start hour
    common_start_hour = df["hour"].mode()[0]
    print("The most common start hour is: " , common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    commonly_used_start_station = df["Start Station"].mode()[0]
    print("The most commonly used start station is: " , commonly_used_start_station)

    # TO DO: display most commonly used end station
    commonly_used_end_station = df["End Station"].mode()[0]
    print("The most commonly used end station is: " , commonly_used_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    group_field = df.groupby(["Start Station","End Station"])
    frequent_combination_of_stations = group_field.size().sort_values
    print("Most frequent combination of Start Station and End Station trip: ", frequent_combination_of_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("Total Travel Time is:", total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("Mean Travel Time: ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df["User Type"].value_counts()
    print("The count of user types from the given fitered data is:" , user_types)
    
    if city != "washington.csv":
        # TO DO: Display counts of gender
        gender = df["Gender"].value_counts()
        print("The count of user gender is:" , gender)

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth = df["Birth Year"].min()
        most_recent_birth = df["Birth Year"].max()
        most_common_birth = df["Birth Year"].mode()[0]
        print("Earliest year of birth is: ", earliest_birth)
        print("Most recent year of birth is: ", most_recent_birth)
        print("Most common year of birth is: ", most_common_birth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
