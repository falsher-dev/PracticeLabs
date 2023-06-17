import numpy as np
import pandas as pd
import matplotlib.pyplot as mp
import seaborn as sb

customers = pd.read_csv('customers.csv') # Считываем дата-сет

print(customers.head(3))
print("Краткое info о нашем дата-сете: \n")
print(customers.info())
print()
print(customers.describe())
print('Средний возраст покупателей :',customers['Age'].mean())
print('Среднее количество детей у покупателей',customers['Family Size'].mean())
print('Самая часто-встречаемая профессия у покупателей:', customers['Profession'].mode())

# проанализируем покупателей по полу
sb.countplot(data=customers, x='Gender')
mp.show()
sb.histplot(data=customers, y='Age', color='blue', edgecolor='black', hue='Gender',bins=10)
mp.show()
# заработок по полу
sb.histplot(data=customers, x='Annual Income ($)',hue='Gender',bins=30000)
mp.show()
# Размер семьи
sb.histplot(data=customers, x='Family Size', color='red', edgecolor='black')
mp.show()
# Тепловая карта всех параметров
sb.heatmap(data=customers.corr(), annot=True)
mp.show()
# Возраст и очки
mp.savefig('scatter.png', dpi=300, bbox_inches='tight')
# Корреляция профессии и зарплаты
grid = sb.FacetGrid(data=customers,col = 'Profession', hue='Profession', col_wrap=3)
grid.map(sb.scatterplot, "Profession", "Annual Income ($)")
mp.show()
# Опыт работы и возраст
sb.residplot(data=customers, x='Age', y='Work Experience',lowess=True,line_kws=dict(color="r"))
mp.show()
# Возраст и потраченные очки
sb.scatterplot(data=customers, x="Age", y="Spending Score (1-100)")
sb.rugplot(data=customers, x="Age", y="Spending Score (1-100)")
mp.show()



