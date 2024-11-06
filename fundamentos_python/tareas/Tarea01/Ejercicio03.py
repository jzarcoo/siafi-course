# Type alias
# A Student is a tuple with a name and a score
Student = tuple[str, float]

# Students
yael: Student = ('Yael', 70.0)
ilse: Student = ('Ilse', 90.0)
eduardo: Student = ('Eduardo', 80.0)

"""
    Grade a student based on their score

    Args:
        student (Student): The student to grade

    Returns:
        str: The grade of the student
"""
def grade(student: Student) -> str:
    score: float = student[1]
    if score <= 100.0 and score >= 90.0:
        return 'A'
    elif score < 90.0 and score >= 80.0:
        return 'B'
    elif score < 80.0 and score >= 70.0:
        return 'C'
    elif score < 70.0 and score >= 60.0:
        return 'D'
    return 'F'

"""
    Main function
"""
def main() -> None:
    for student in [yael, ilse, eduardo]:
        print(f'{student[0]} has a grade of {grade(student)}')

"""
    Entry point
"""    
if __name__ == '__main__':
    main()