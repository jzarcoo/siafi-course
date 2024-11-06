# Exercise 6. Create a DataFrame with columns name, age, and city for 5 people (put whatever data you want).
# Add a new column called occupation with values ​​of your choice.

import pandas as pd

"""
    Main function.
"""
def main() -> None:
    data: dict[str, list] = {
        'Name': ['Bob', 'Alice', 'Michelle', 'Mike', 'Taylor'],
        'Age': list(range(18, 23)),
        'City': ['New York', 'Pennsylvania', 'California', 'Texas', 'Florida']
    }
    df: pd.DataFrame = pd.DataFrame(data)
    print('DataFrame:')
    print(df, '\n')
    df['Occupation'] = ['Software Engineer', 'Data Scientist', 'Web Developer', 'Network Engineer', 'Database Administrator']
    print('DataFrame with Occupation column:')
    print(df)

"""
    Entry point for the script.
"""
if __name__ == '__main__':
    main()