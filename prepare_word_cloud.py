import pandas as pd
from os import path
import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud

df = pd.read_csv("reviews.csv")
print(df.head())

# to check if there are any null values - optional
null_values = df.isna().sum()
print("Printing null values if any" + str(null_values))

# split word "GAME" from each category values
# text = " ".join(cat.split()[1] for cat in df.category)
# print(text)
text = " ".join(rev for rev in df.reviews)
print(text)

# create word cloud
word_cloud = WordCloud(collocations = False, background_color = 'white').generate(text)

# plot the word cloud 
plt.imshow(word_cloud, interpolation='bilinear')
plt.axis("off")
plt.show()