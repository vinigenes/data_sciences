import pandas as pd

#List
list_names = ['Any', 'Jhon', 'Michael']
print(f'List names: \n{list_names}')
print(f'First element: {list_names[0]}')

#Dictionary
dictionary_person = {
    'name': 'Any',
    'age': '21',
    'city': 'Camaracity'
}
print(f'Dictionary person: {dictionary_person}')
print(f'Frist name: {dictionary_person["name"]}')

#List 
list_dictionary = [
    {'name': 'Any', 'age': 21, 'city': 'Camaracity'},
    {'name': 'Jhon', 'age': 22, 'city': 'Camaracity'},
    {'name': 'Michael', 'age': 25, 'city': 'Camaracity'}
]

#Data Frame: bidimensional data estructure
df = pd.DataFrame(list_dictionary)
print(f'{df}\n')

#Select column
print(f"{df['name']}\n")

#Select seceral colums
print(f"{df[['name', 'age']]}\n")

#Select line by indexe
print(f'First line:{df.iloc[0]}\n')

#Add new column
df['salary'] = [1555, 2000, 3000]
print(f'{df}\n')

#Add new record
df.loc[len(df)]= {'name': 'Mike', 'age': 25, 'city': 'Camaracity', 'salary': 2000}
print(f'{df}\n')

#Remove column
df.drop('salary', axis=1, inplace= True)
print(f'{df}\n')

#Filter by age
filter_age = df[df['age'] <25 ]
print(f'Filter by age: \n{filter_age}\n')

#Salving the Dataframe in a CSV file
df.to_csv('data.csv', index= False)

#Reading a csv file in a Dataframe
df_read = pd.read_csv('data.csv')
print(f'CSV reading: \n{df_read}')