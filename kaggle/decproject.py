import pandas as p
import matplotlib.pyplot as pl
import seaborn as sn

data = p.read_csv('appstore_games.csv')
print(data)

#check columns
print(data.columns)

#check which has more null values
print(data.isnull().sum())

#drop null values
data=data.dropna()

#Identify the genres which are more significant and do simple analysis for the distribution according to genres.
best_genres = list(data["Genres"].value_counts().head(10).index)
data[data["Genres"].isin(best_genres)]["Genres"].value_counts().plot.bar(figsize=(8,5))
pl.title("Best Genres")
pl.show()

#Identify Which genres have higher user ratings.
fig, hp = pl.subplots(1,2, figsize=(15,5))
sn.barplot(data=data[data["Genres"].isin(best_genres)], x="Average User Rating" ,y="Genres",ax=hp[0]).set_xticklabels(hp[0].get_xticklabels(), rotation=90)
sn.barplot(data=data[data["Genres"].isin(best_genres)], x="User Rating Count" ,y="Genres",ax=hp[1]).set_xticklabels(hp[1].get_xticklabels(), rotation=90)
hp[0].set_title("User Rating Count of games in each genre")
hp[1].set_title("Average rating of games in each genre")
pl.show()

#Identify Average User Rating Based on Pricing
sn.barplot(data=data,x="Price",y ="Average User Rating")
pl.title("Average user rating based on price range")
pl.show()
