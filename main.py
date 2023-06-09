

import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('cond4.csv', sep = ',')


# топ 10 по рейтингу
print("top by  ratings")
data2 = data.nlargest(10, 'ratings')
data = data.reset_index()
for index, row in data2.iterrows():
    print(row['name'],row['ratings'])

data2.plot(kind='bar', x='name', y='ratings', title='ratings')
plt.show()

print("top by discount price")
# топ 10 по цене
data2 = data.nsmallest(10, 'discount_price EUR')
for index, row in data2.iterrows():
    print(row['name'],row['discount_price EUR'])

data2.plot(kind='bar', x='name', y='discount_price EUR', title='discount price EUR')
plt.show()

# топ 10 по количеству рейтингов
print("top by number of ratings")
data2 = data.nlargest(10, 'no_of_ratings')
for index, row in data2.iterrows():
    print(row['name'],row['no_of_ratings'])

data2.plot(kind='bar', x='name', y='no_of_ratings', title='No of Ratings')

# корреляция
print("correlation between ratings and discount price EUR")
print(data['ratings'].corr(data['discount_price EUR']))
# Display the plot

plt.show()





