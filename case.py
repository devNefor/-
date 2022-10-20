import pandas as pd 
import matplotlib.pyplot as plt 
 
df = pd.read_csv('menu.csv') 
 
print('В завтраках каллорий больше чем в десертах:') 
 
calories_breakfast = df.groupby(by = 'Category')['Calories'].mean() 
print('Калорий в завтраках', round(calories_breakfast['Breakfast'], 2)) 
calories_dessert = df.groupby(by = 'Category')['Calories'].mean() 
print('Калорий в десертах', round(calories_dessert['Desserts'], 2)) 
 
s = pd.Series(data=[calories_breakfast['Breakfast'], calories_dessert['Desserts']], 
    index=['калории в завтраках', 'калории в десертах']) 
s.plot(kind='pie', y='Calories') 
plt.show() 
 
print('Максимальная порция свинины и говядины, равна максимальной порции курицы и рыбы') 
 
serving_size_pork = df.groupby(by = 'Category')['Serving Size'].max() 
print('максимальная порция говядины и свинины:', serving_size_pork['Beef & Pork']) 
serving_size_chicken = df.groupby(by = 'Category')['Serving Size'].max() 
print('максимальная порция курицы и рыбы:', serving_size_chicken['Chicken & Fish']) 
 
a = pd.Series(data=[270, 270], 
    index=['максимальная порция говядины и свинины', 'максимальная порция курицы и рыбы']) 
a.plot(kind='bar') 
plt.show() 
 
calories = round(df.groupby(by = 'Category')['Calories'].mean())  
print('Среднее число калорий в напитках', calories['Smoothies & Shakes'])  
print('Среднее число калорий в бургерах', calories['Desserts'])  
print('Средний процент крепкости и калорий в Кофе и Чая', calories['Coffee & Tea'])  
calories.plot(kind = 'barh')  
plt.xlabel('Calories')  
plt.show()