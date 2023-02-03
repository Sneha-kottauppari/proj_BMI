# Sneha kottauppari
#roll no: 2021501022

# imports
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

#1. fetching data from url

url= "http://wiki.stat.ucla.edu/socr/index.php/SOCR_Data_Dinov_020108_HeightsWeights"
response=requests.get(url)

if response.status_code==200:
    data=response.content
    # print(data)
else:
    print("request failed")


# 2. Extract tabular data from the web content**

soup=BeautifulSoup(data,'html.parser')
# print(soup.prettify)
table=soup.find_all("table")[1]
# print(table)

# creating dataframe
df=pd.read_html(str(table))[0]
df = df.iloc[:, [0, 1, 2]]
df.columns = ['index', 'heights', 'weights']
df_heights_weights = df
print(df_heights_weights)


# maximum height

max_height = df_heights_weights['heights'].max()
print("Max height:", max_height)


# maximum weight

max_weight = df_heights_weights['weights'].max()
print("Max height:", max_weight)

# plot sorted data


df_heights_weights_sorted = df_heights_weights.sort_values('weights')
df_plot = df_heights_weights_sorted.head(15)

plt.plot(df_plot['weights'], df_plot['heights'], 'o')
plt.xlabel('Weights')
plt.ylabel('Heights')
plt.title('Height vs Weight (first 15 entries)')
# plt.show()


#convert height to  metere and weight tok kgs


df_metric = df_heights_weights.copy()
df_metric['heights'] = df_metric['heights'] / 39.37
df_metric['weights'] = df_metric['weights'] * 0.453592

#BMIcolumn
df_metric['BMI'] = df_metric['weights'] / (df_metric['heights'] ** 2)

print(df_metric)

#count of obesity class 2


count = ((35 <= df_metric['BMI']) & (df_metric['BMI'] <= 39.9)).sum()


print (count)
