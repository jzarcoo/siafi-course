"""
    Main function. Print the even numbers from 1 to 100
"""
def main() -> None:
    for i in range(1, 101):
        if i % 2 == 0:
            print(i)

"""
    Entry point for the program.
"""
if __name__ == '__main__':
    main()