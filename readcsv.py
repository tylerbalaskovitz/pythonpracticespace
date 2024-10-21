import pandas as pd 

df = pd.read_csv("output.csv")
print(df)
df['Bonus'] = df['Salary'] * 0.10
average_salary= df['Salary'].mean()
average_df = pd.DataFrame({'Average Salary': [average_salary]})
average_df.to_csv("average_salary",index=False)
df.to_csv("bonus_included", index=False)
print(df)
