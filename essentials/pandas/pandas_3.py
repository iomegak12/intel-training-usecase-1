import pandas as pd

student_scores = {
    "Ramkumar": 100,
    'Sunil': 500,
    'Sugata': 600,
    'Sherif': 900,
    'Shah': 650,
}

series = pd.Series(student_scores, index=student_scores.keys())

print(series)
