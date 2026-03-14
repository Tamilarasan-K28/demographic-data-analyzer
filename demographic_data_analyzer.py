import pandas as pd


def calculate_demographic_data(print_data=True):

    # Read dataset
    df = pd.read_csv(
        "adult.data.csv",
        header=None,
        skipinitialspace=True,
        names=[
            'age','workclass','fnlwgt','education','education-num',
            'marital-status','occupation','relationship','race','sex',
            'capital-gain','capital-loss','hours-per-week',
            'native-country','salary'
        ]
    )

    # Clean spaces
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    # 1. Race count
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage with Bachelor's
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # 4. Higher education
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education

    # 5. Percentage rich with higher education
    higher_education_rich = round(
        (df[higher_education]['salary'] == '>50K').mean() * 100, 1
    )

    # 6. Percentage rich without higher education
    lower_education_rich = round(
        (df[lower_education]['salary'] == '>50K').mean() * 100, 1
    )

    # 7. Minimum work hours
    min_work_hours = df['hours-per-week'].min()

    # 8. Percentage rich among min workers
    num_min_workers = df[df['hours-per-week'] == min_work_hours]

    rich_percentage = round(
        (num_min_workers['salary'] == '>50K').mean() * 100, 1
    )

    # 9. Country with highest percentage of >50K
    country_salary = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_total = df['native-country'].value_counts()

    country_percentage = (country_salary / country_total) * 100

    highest_earning_country = country_percentage.idxmax()
    highest_earning_country_percentage = round(country_percentage.max(), 1)

    # 10. Top occupation in India
    india_rich = df[
        (df['native-country'] == 'India') &
        (df['salary'] == '>50K')
    ]

    top_IN_occupation = india_rich['occupation'].value_counts().idxmax()

    # Print results
    if print_data:
        print("Race count:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors:", percentage_bachelors)
        print("Higher education rich:", higher_education_rich)
        print("Lower education rich:", lower_education_rich)
        print("Min work hours:", min_work_hours)
        print("Rich % among min workers:", rich_percentage)
        print("Country with highest earners:", highest_earning_country)
        print("Highest earning country %:", highest_earning_country_percentage)
        print("Top occupation in India:", top_IN_occupation)

    return {
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