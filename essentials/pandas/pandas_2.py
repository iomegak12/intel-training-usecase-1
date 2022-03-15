import pandas as pd

student_scores = {
    1: 100,
    2: 500,
    3: 600,
    4: 900,
    5: 650
}

series = pd.Series(student_scores, index = student_scores.keys())

print(series)