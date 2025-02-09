import csv
import pandas as pd
file='annual.csv'
df=pd.read_csv(file)
df_cleaned=df.dropna().drop_duplicates()
df_new=df_cleaned.drop(columns=['Industry_code_NZSIOC'])
df_new.to_csv('annual_cleaned.csv',index=False)
with open('annual_cleaned.csv','r') as f:
    csv_reader=csv.reader(f)
    for row in csv_reader:
        print(row)
        
