"""Welcome to the grade calculator app.\n
The program asks for your test scores and returns your grade."""

test_score = int(input("What is your test score, it should not be over 100: "))

def get_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 40:
        return "D"
    elif score < 40:
        return "F"
    else:
        return "Enter a valid score!"

print(get_grade(test_score))