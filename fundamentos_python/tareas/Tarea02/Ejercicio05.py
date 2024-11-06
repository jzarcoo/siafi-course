# Exercise 5. Create a series of 10 elements with the numbers from 1 to 10.
# Change the indices of the series to the names of the first 10 countries according to their population.

import pandas as pd

"""
    Main function.
"""
def main() -> None:
    countries: list[str] = [
        'China',
        'India',
        'United States',
        'Indonesia',
        'Pakistan',
        'Nigeria',
        'Brazil',
        'Bangladesh',
        'Russia',
        'Mexico'
    ]
    series: pd.Series = pd.Series(range(1, 11))
    print('Serie from 1 to 10:')
    print(series)
    series.index = countries
    series.name = 'Countries most populated'
    print('Serie with countries as index:')
    print(series)

"""
    Entry point for the script.
"""
if __name__ == '__main__':
    main()