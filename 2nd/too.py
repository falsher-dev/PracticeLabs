import pandas
import statistics

def formatMap(format, map):
    keys = map.keys()
    values = map.values
    maxIndex = min(keys.size, values.size)
    ret = ""
    for i in range (0, maxIndex, 1):
        ret += format % (keys[i], values[i])
    return ret;

t = pandas.read_csv('train.csv') #import data from csv
print(t.describe()) #statistics for all numerical features
print('\n');

print(t.describe(include=['O'])) #statics for all not-numerical features
print('\n');

print(
    "Passengers count: %d" %
    len(t["PassengerId"])
)
av_age = t['Age'].mean()
print(
    'Average age: %-.7g' %
    av_age
)
print(
    'Median age: %-.7g' %
    t['Age'].median()
)
print(
    'Age mode: %d' %
    statistics.mode(t['Age'].values)
)
print(
    'Average of siblings on board: %-.7g' %
    t['SibSp'].mean()
)
print(
    'Average of relatives on board: %-.7g' %
    (t['SibSp'] + t['Parch']).mean()
)
print(
    'Survived passengers: %d' %
    len(t[t['Survived'] == 1])
)
print(
    'Losted passengers: %d' %
    len(t[t['Survived'] == 0])
)
print(
    'Passengers in each classes:%s' %
    formatMap(
        "\n\tClass %d: %d",
        t['Pclass'].value_counts().sort_index()
    )
)
print(
    'Average ticket price in each classes:%s' %
    formatMap(
        "\n\tClass %d: %.7g$",
        t.groupby('Pclass')['Fare'].mean().sort_index()
    )
)
print(
    'Average ticket price for each Sex:%s' %
    formatMap(
        "\n\t%s: %.7g$",
        t.groupby('Sex')['Fare'].mean()
    )
)
print(
    'Passengers with relatives: %d' %
    len(t[(t['SibSp'] > 0) | t['Parch'] > 0])
)
print(
    'Average of ticket price of survived passengers: %-.7g' %
    t[t['Survived'] == 1]['Fare'].mean()
)
print(
    'The number of empty values in each column:%s' %
    formatMap(
        "\n\t%s: %d",
        t.isnull().sum()
    )
);
av_age = round(av_age)
t['Age'].fillna(av_age, inplace=True)
t['HaveRelatives'] = t['SibSp'] + t['Parch'] > 0
mode_port = statistics.mode(t['Embarked'].values)
print("Most popular port of departure: %s" % (
    "Cherbourg" if
        mode_port == 'C' else
    "Queenstown" if
        mode_port == 'Q' else
    "Southampton" if
        mode_port == 'S' else
    "N/D"
))