import pandas as pd

fruitinfo = {
    'Apples': [35, 41],
    'Bananas': [21, 34]
}

df = pd.DataFrame(fruitinfo, index=['2017 Sales', '2018 Sales'])


df.to_csv('fruit.csv')

print("Data has been written to 'fruit.csv'")