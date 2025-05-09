import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("data/demographic.csv")
    
    # How many people of each race are represented in this dataset?
    race_count = df['race'].value_counts()
    
    # What is the average age of men?
    average_age_men = round(df.loc[df['sex'] == 'Male', 'age'].mean(), 1)
    
    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(len(df[df['education'] == 'Bachelors']) / len(df) * 100, 1)
    
    # What percentage of people with advanced education make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    
    # Advanced education: Bachelors, Masters, or Doctorate
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    
    # Percentage with salary >50K
    higher_education_rich = round(len(higher_education[higher_education['salary'] == '>50K']) / len(higher_education) * 100, 1)
    lower_education_rich = round(len(lower_education[lower_education['salary'] == '>50K']) / len(lower_education) * 100, 1)
    
    # What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()
    
    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(len(num_min_workers[num_min_workers['salary'] == '>50K']) / len(num_min_workers) * 100, 1)
    
    # What country has the highest percentage of people that earn >50K?
    country_stats = df.groupby('native-country')['salary'].apply(
        lambda x: round((x == '>50K').sum() / len(x) * 100, 1)
    ).sort_values(ascending=False)
    
    highest_earning_country = country_stats.index[0]
    highest_earning_country_percentage = country_stats.iloc[0]
    
    # Identify the most popular occupation for those who earn >50K in India
    india_high_earners = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_high_earners['occupation'].value_counts().idxmax() if not india_high_earners.empty else "No data available"
    
    # Create a dictionary to return all results
    results = {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
    
    # Print results if requested
    if print_data:
        print("Race Count:\n", race_count)
        print("Average Age of Men:", average_age_men)
        print("Percentage with Bachelors degrees:", percentage_bachelors, "%")
        print("Percentage with higher education that earn >50K:", higher_education_rich, "%")
        print("Percentage without higher education that earn >50K:", lower_education_rich, "%")
        print("Min work hours:", min_work_hours)
        print("Percentage of rich among those who work fewest hours:", rich_percentage, "%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print("Highest percentage of rich people in country:", highest_earning_country_percentage, "%")
        print("Top occupations in India:", top_IN_occupation)
    
    return results

# Call the function to calculate and print the results
calculate_demographic_data()
