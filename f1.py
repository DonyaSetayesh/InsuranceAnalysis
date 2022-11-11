from hashlib import new
from os import system
from statistics import mean
import string
from IPython.display import display
from tokenize import Double
import pandas as pd
import numpy as np
df = pd.read_csv('train.csv')
Number_of_Rows =len(df)
Number_of_Coloumns = len(df.columns)
print(Number_of_Rows)
print(Number_of_Coloumns)

column_name = "AnnualIncome"
column_sum = df[column_name].sum()
Csum = column_sum/Number_of_Rows
print(int(Csum))
 
n=df['EverTravelledAbroad'].value_counts(ascending=True)
print(n)


Number_of_Traveled_abroad=df.EverTravelledAbroad.value_counts().Yes
print(Number_of_Traveled_abroad)

Number_of_Employement_TypeG=df['Employment Type'].value_counts()['Government Sector']
print(Number_of_Employement_TypeG)
Number_of_Employement_TypeP=df['Employment Type'].value_counts()['Private Sector/Self Employed']
print(Number_of_Employement_TypeP)

if Number_of_Employement_TypeP > Number_of_Employement_TypeG:
    
    percentage =(Number_of_Employement_TypeP/Number_of_Rows)*100
    format_float = "{:.2f}".format(percentage)
    print('Private Sector/Self Employed',format_float)
else:
    percentage =(Number_of_Employement_TypeG/Number_of_Rows)*100
    format_float = "{:.2f}".format(percentage)
    print('Government Sector',format_float)



filtered_values = np.where((df['ChronicDiseases']==1) & (df['TravelInsurance'].str.startswith('Y')) )
filtered_values_chronic = np.where((df['ChronicDiseases']==1))

display(df.loc[filtered_values])  
Number_of_Rows_CHRONIC_INSURE =len(df.loc[filtered_values])
Number_of_Rows_CHRONIC= len(df.loc[filtered_values_chronic])
print('this is' , Number_of_Rows_CHRONIC_INSURE)
print(Number_of_Rows_CHRONIC)

percentage_Chronic_Insured= Number_of_Rows_CHRONIC/Number_of_Rows_CHRONIC_INSURE
print("percentage_Chronic_Insured", percentage_Chronic_Insured)

input()