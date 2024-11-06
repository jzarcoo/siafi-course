# Exercise 7. Create a DataFrame with 5 cities and their temperature in Celsius.
# Add a new column that converts the temperatures to Fahrenheit.

import pandas as pd
    
"""
    Main function.
"""
def main() -> None:
    cities: list[str] = ['Lima', 'Arequipa', 'Cusco', 'Trujillo', 'Piura']
    temperatures: list[float] = [20.5, 25.3, 10.0, 30.0, 35.0]
    data: dict[str, list] = {
        'City': cities,
        'Temperature (C)': temperatures
    }
    df: pd.DataFrame = pd.DataFrame(data)
    print('DataFrame:')
    print(df, '\n')

    df['Temperature (F)'] = (df['Temperature (C)'] * 9/5) + 32
    print('DataFrame with Temperature (F) column:')
    print(df)

"""
    Entry point for the script.
"""
if __name__ == '__main__':
    main()