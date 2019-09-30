def calculate(a, b, operation):
    answers = {
        'sum': a + b,
        'div': a / b,
        'sub': a - b,
        'mult': a * b,
        'floor div': a // b,
        'mod': a % b,
        'exp': a ** b
    }
    return answers[operation]


print(calculate(5, 5, 'mult'))