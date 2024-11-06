# Exercise 8. From the file sales.csv (In classroom: Class04 Numpy and Pandas), load the dataframe and calculate the average sales

import pandas as pd

"""
    Main function.
"""
def main() -> None:
    df: pd.DataFrame = pd.read_csv('ventas.csv')
    print('DataFrame from ventas.csv:')
    print(df, '\n')

    promedio_ventas: float = df['Ventas'].mean()
    print('Promedio de las Ventas:', promedio_ventas)

"""
    Entry point for the script.
"""
if __name__ == '__main__':
    main()