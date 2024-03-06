# Complete analysis of employee's salary data

import pandas as pd
df=pd.read_csv('Salaries.csv')
## Displaying data 
print(df.to_string())
## Total rows and cols 
print(df.shape)
## Displaying top 10 entries
print('Head upto 10 entries')
print(df.head(10))
## Displaying last 15 entries
print('Tail upto 15 entries')
print(df.tail(15))



## Determining rows and cols in dataset
print('Total rows:',df.shape[0])
print('Total cols:',df.shape[1])
print('Total rows X cols:',df.shape)

## Evaluating and performing max and min salary of different gender employees
print(df['sex'].unique())
print(df['sex'].value_counts())
s1=df[df['sex']=='Male']
s2=df[df['sex']=='Female']
print('Which male professor has highest salary',s1['salary'].max())
print('Which female professor has highest salary',s2['salary'].max())
print('Which male professor has highest salary',s1['salary'].min())
print('Which female professor has highest salary',s2['salary'].min())
print('Professor which has highest salary:\n',df[df['salary']==df['salary'].max()])
print('Professor which has lowest salary:\n',df[df['salary']==df['salary'].min()])


## Determine mean of phd and salary data
salary_data=df['salary']
phd_data=df['phd']
print(salary_data,'\n')
print('Mean value of salary column')
mean_salary=salary_data.mean()
mean_phd=phd_data.mean()
print('Mean of salary:',mean_salary,'\n')
print('Mean of phd:',mean_phd,'\n')

## Dealing with missing values 
print('Which attribute has missing values either true or false')
print(df.isnull().any(axis=0))
df['salary']=df['salary'].fillna(mean_salary)
df['phd']=df['phd'].fillna(mean_phd)
print('Which attribute has missing values either true or false')
print(df.isnull().any(axis=0))

## Count total records of different Gender/Sex
print(df['sex'].value_counts())

## Count total records of different rank
print(df['rank'].value_counts())

## Displaying data related to specific gender
senior_df=df[df['rank']=='AssocProf']
print(senior_df.to_string())
junior_df=df[df['rank']=='Prof']
print(junior_df.to_string())


