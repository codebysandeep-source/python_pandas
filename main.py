import pandas as pd  #Pandas” stands for Panel Data and is the core library for data manipulation and data analysis. . It consists of single and multi-dimensional data-structures for data-manipulation.
#to install ->  pip install pandas

# DataDrame()    ->  A DataFrame is a data structure that organizes data into a 2-dimensional table of rows and columns, much like a spreadsheet. DataFrames are one of the most common data structures used in modern data analytics because they are a flexible and intuitive way of storing and working with data.
student_table = pd.DataFrame({
  'NAME': ['Sandeep','Mukesh','Dheeraj','Anup','Rahul','Jamil'],
  'AGE': [23,22,24,23,24,35],
  'ADDRESS': ['Sikkim','Siliguri','UP','Darjeeling','Lucknow','Goa']
  })

#print(student_table)

# read_csv - read_csv is used to load a CSV file as a pandas dataframe. CSV stand for Comma-Separated Values 
csv_table = pd.read_csv("students.csv")  # Select * from students.csv
#print(csv_table)

name = csv_table[['NAME']] # Select NAME from students.csv
#print(name)

age = csv_table[['AGE']]   # Select AGE from students.csv
#print(age)

name_age = csv_table[['NAME','AGE']]  # Select NAME,AGE from students.csv
#print(name_age)

age23 = csv_table[csv_table['AGE']==23]   #select * from students.csv where age is 23
print(age23)


