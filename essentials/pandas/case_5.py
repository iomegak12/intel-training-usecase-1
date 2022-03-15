import pandas as pd
import numpy as np

fileName = './Churn_Modelling.csv'

pd.set_option('display.max_columns', None)
pd.set_option('display.precision', 2)

df = pd.read_csv(fileName)

# returns correlation between columns in the dataframe, which is used for machine
# learning predictive analytics in terms of chooing features required for predictions

# print(df.corr())

# print(df.count())

# print(df["Geography"].unique())

# print(df["Gender"].value_counts(dropna = True))

# print(df.sample(n = 10)) # sampling

# print(df.nlargest(5, "Balance") [["RowNumber", "Balance"]]) # select and order top n entries


# Selected and order Bottom n entries
# print(df.nsmallest(5, "EstimatedSalary")[["RowNumber", "Balance", "EstimatedSalary"]])

# Executing a query with filter conditions and top 5 records
# print(df.query("(Gender == 'Male') and (Age < 23) and (EstimatedSalary >= 10000)").head(5))

# filteredDateFrame = df.query("(Gender == 'Male') and (Age < 23) and (EstimatedSalary >= 10000)")
# print(filteredDateFrame[["RowNumber", "Gender", "Age", "EstimatedSalary"]])

# filteredDateFrame["NewEstimatedSalary"] = filteredDateFrame["EstimatedSalary"] * 1.1

# outputFileName = 'out.csv'
# filteredDateFrame.to_csv(outputFileName)

searchPattern = input("Enter Search String ...")
inputGender = "Male"
inputSearchString = f"^[{searchPattern}]"
inputAge = 23
inputEstimatedSalary = 10000

queryString = f"(Gender == '{inputGender}') and (Surname.str.contains('{inputSearchString}')) and (Age >= {inputAge}) and (EstimatedSalary >= {inputEstimatedSalary})"
filteredDateFrame = df.query(queryString)
print(filteredDateFrame[["Gender", "Surname", "Age", "EstimatedSalary"]].head(5))