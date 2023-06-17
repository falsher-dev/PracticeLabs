import pandas as pd

#1
animals_data = {
    'Name':     ['Lion',        'Tiger',    'Elephant',     'Giraffe',      None        ],
    'Species':  ['Carnivore',   None,       'Carnivore',    'Herbivore',    'Herbivore' ],
    'Weight':   [190,           160,        600,            1000,           None        ],
    'Count':    [5,             4,          1,              8,              15          ]
}
df = pd.DataFrame(
    animals_data,
    columns=['Name', 'Species', 'Weight', 'Count']
)
print(df)
print("\n")

#2
df.to_csv('file.csv', index=False)

#3
print("Top and bottom lines:")
print(df.head(1))
print(df.tail(1))
print("\n")

print("Describe:")
print(df.describe())
print("\nColumn 'Species':")
print(df['Species'])
print("\n")

print("Rows with zero-based indexes from 1 to 3 (not incl.):")
print(df[1:3])
print("\n")

print("Groped and Aggregated:")
print(df.groupby('Name').agg({'Weight': 'mean'}));
print("\n")

print("Delete rows with n/d:")
print(df.dropna())
print("\n")

print('Replace cells with n/d to "No data":')
df = df.fillna("No data")
print(df)
print("\n")

print('Sort by "Count":')
print(df.sort_values(by='Count', ascending=True))
print("\n")

print('Filtered data: (Weight > 500):')
df.at[4, 'Weight'] = 700;
print(df[
    df['Weight'] > 500
].sort_values(by='Weight', ascending=True))
print("\n")

print('Rename col "Weight" to "Heft":')
print(df.rename(
    columns={'Weight': 'Heft'}
))