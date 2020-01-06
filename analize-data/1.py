import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.linear_model import LinearRegression
import seaborn as sns

pd.set_option('display.max_columns', 28)
pd.set_option('display.width', 2000)

# Read the online file by the URL provides above, and assign it to variable "df"
path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/automobileEDA.csv'
# headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
#          "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
#          "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
#          "peak-rpm","city-mpg","highway-mpg","price"]
# df = pd.read_csv(path, names=headers)
df = pd.read_csv(path)
lm = LinearRegression()
# print(lm)


# print(df.dtypes)
# replace "?" to NaN
df.replace("?", np.nan, inplace = True)
missing_data = df.isnull()
# print("headers\n", headers)
# df.columns = headers
# print(df.columns)
print(df.dtypes)
# print(df.describe(include = "all"))


# for column in missing_data.columns.values.tolist():
#     print(column)
#     print (missing_data[column].value_counts())
#     print("")

# avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
# df["normalized-losses"].replace(np.nan, avg_norm_loss, inplace=True)
# print("Average of normalized-losses:", avg_norm_loss)

# avg_bore=df['bore'].astype('float').mean(axis=0)
# # print("Average of bore:", avg_bore)
# df["bore"].replace(np.nan, avg_bore, inplace=True)

# avg_stroke = df['stroke'].astype('float').mean(axis=0)
# df['stroke'].replace(np.nan,avg_stroke,inplace=True)
#
# avg_horsepower = df['horsepower'].astype('float').mean(axis=0)
# # print("Average horsepower:", avg_horsepower)
# df['horsepower'].replace(np.nan, avg_horsepower, inplace=True)

# avg_peakrpm=df['peak-rpm'].astype('float').mean(axis=0)
# print("Average peak rpm:", avg_peakrpm)
# df['peak-rpm'].replace(np.nan, avg_peakrpm, inplace=True)

#   most common type
# print(df['num-of-doors'].value_counts().idxmax())

#replace the missing 'num-of-doors' values by the most frequent
df["num-of-doors"].replace(np.nan, "four", inplace=True)

# simply drop whole row with NaN in "price" column
df.dropna(subset=["price"], axis=0, inplace=True)

# reset index, because we droped two rows
df.reset_index(drop=True, inplace=True)

df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
df[["normalized-losses"]] = df[["normalized-losses"]].astype("int")
df[["price"]] = df[["price"]].astype("float")
# df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")

# Convert mpg to L/100km by mathematical operation (235 divided by mpg)
df['city-L/100km'] = 235/df["city-mpg"]
#transform mpg to L/100km in the column of "highway-mpg", and change the name of column to "highway-L/100km".
df['highway-L/100km'] = 235/df["highway-mpg"]
# rename column name from "highway-mpg" to "highway-L/100km"
df.rename(columns={'"highway-mpg"':'highway-L/100km'}, inplace=True)

# replace (original value) by (original value)/(maximum value)
# df['length'] = df['length']/df['length'].max()
# df['width'] = df['width']/df['width'].max()
df['height'] = df['height']/df['height'].max()


df["horsepower"]=df["horsepower"].astype(int, copy=True)

# check your transformed data
# print(df[["horsepower"]].dtypes)

# set x/y labels and plot title
# plt.xlabel("horsepower")
# plt.ylabel("count")
# plt.title("horsepower bins")

bins = np.linspace(min(df["horsepower"]), max(df["horsepower"]), 4)
group_names = ['Low', 'Medium', 'High']

df['horsepower-binned'] = pd.cut(df['horsepower'], bins, labels=group_names, include_lowest=True )
# print(df[['horsepower','horsepower-binned']].head(20))

#Lets see the number of vehicles in each bin.
df["horsepower-binned"].value_counts()

a = (0,1,2)

# draw historgram of attribute "horsepower" with bins = 3
# plt.hist(df["horsepower"], bins = 3)

# set x/y labels and plot title
# plt.xlabel("horsepower")
# plt.ylabel("count")
# plt.title("horsepower bins")

# "gas" or "diesel". Regression doesn't understand words, only numbers.
df.columns
dummy_variable_1 = pd.get_dummies(df["fuel-type"])
dummy_variable_1.rename(columns={'fuel-type-diesel':'gas', 'fuel-type-diesel':'diesel'}, inplace=True)
# merge data frame "df" and "dummy_variable_1"
df = pd.concat([df, dummy_variable_1], axis=1)
# drop original column "fuel-type" from "df"
df.drop("fuel-type", axis = 1, inplace=True)

# get indicator variables of aspiration and assign it to data frame "dummy_variable_2"
dummy_variable_2 = pd.get_dummies(df['aspiration'])
# change column names for clarity
dummy_variable_2.rename(columns={'std':'aspiration-std', 'turbo': 'aspiration-turbo'}, inplace=True)
df = pd.concat([df, dummy_variable_2], axis=1)
# drop original column "fuel-type" from "df"
df.drop("aspiration", axis = 1, inplace=True)

# df.to_csv('clean_df.csv')
# plt.pyplot.show()

# sns.regplot(x="engine-size", y="price", data=df)
# plt.ylim(0,)
# plt.show()
# print(df[["engine-size", "price"]].corr())

# sns.regplot(x="highway-mpg", y="price", data=df)
# plt.ylim(0,)
# plt.show()
# print(df[['highway-mpg', 'price']].corr())

# sns.regplot(x="stroke", y="price", data=df)
# plt.ylim(0,)
# plt.show()
# print(df[['stroke','price']].corr())

# sns.boxplot(x="drive-wheels", y="price", data=df)
# plt.ylim(0,)
# plt.show()

# print(df.describe(include=['object']))

drive_wheels_counts = df['drive-wheels'].value_counts().to_frame()
drive_wheels_counts.rename(columns={'drive-wheels': 'value_counts'}, inplace=True)
drive_wheels_counts.index.name = 'drive-wheels'
# print(drive_wheels_counts)

# engine-location as variable
engine_loc_counts = df['engine-location'].value_counts().to_frame()
engine_loc_counts.rename(columns={'engine-location': 'value_counts'}, inplace=True)
engine_loc_counts.index.name = 'engine-location'
# print(engine_loc_counts.head(10))

# print(df['drive-wheels'].unique())
df_group_one = df[['drive-wheels','body-style','price']]
df_group_one = df_group_one.groupby(['drive-wheels'],as_index=False).mean()
# print(df_group_one)

# grouping results
df_gptest = df[['drive-wheels','body-style','price']]
grouped_test1 = df_gptest.groupby(['drive-wheels','body-style'],as_index=False).mean()
# print(grouped_test1)

grouped_pivot = grouped_test1.pivot(index='drive-wheels',columns='body-style')
grouped_pivot = grouped_pivot.fillna(0) #fill missing values with 0
# print(grouped_pivot)

# fig, ax = plt.subplots()
# im = ax.pcolor(grouped_pivot, cmap='RdBu')
# #label names
# row_labels = grouped_pivot.columns.levels[1]
# col_labels = grouped_pivot.index
# #move ticks and labels to the center
# ax.set_xticks(np.arange(grouped_pivot.shape[1]) + 0.5, minor=False)
# ax.set_yticks(np.arange(grouped_pivot.shape[0]) + 0.5, minor=False)
# #insert labels
# ax.set_xticklabels(row_labels, minor=False)
# ax.set_yticklabels(col_labels, minor=False)
# #rotate label if too long
# plt.xticks(rotation=90)
# fig.colorbar(im)
# plt.show()

pearson_coef, p_value = stats.pearsonr(df['wheel-base'], df['price'])
# print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)

pearson_coef, p_value = stats.pearsonr(df['horsepower'], df['price'])
# print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)

pearson_coef, p_value = stats.pearsonr(df['length'], df['price'])
# print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)

pearson_coef, p_value = stats.pearsonr(df['curb-weight'], df['price'])
# print( "The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)

grouped_test2=df_gptest[['drive-wheels', 'price']].groupby(['drive-wheels'])
# print(grouped_test2.head(2))
# print(df_gptest)

grouped_test2.get_group('4wd')['price']
# ANOVA
f_val, p_val = stats.f_oneway(grouped_test2.get_group('fwd')['price'], grouped_test2.get_group('rwd')['price'],
                              grouped_test2.get_group('4wd')['price'])

# print("ANOVA results: F=", f_val, ", P =", p_val)

f_val, p_val = stats.f_oneway(grouped_test2.get_group('fwd')['price'], grouped_test2.get_group('rwd')['price'])

# print("ANOVA results: F=", f_val, ", P =", p_val)

f_val, p_val = stats.f_oneway(grouped_test2.get_group('4wd')['price'], grouped_test2.get_group('rwd')['price'])

# print("ANOVA results: F=", f_val, ", P =", p_val)

X = df[['highway-mpg']]
Y = df['price']
lm.fit(X,Y)
Yhat=lm.predict(X)
print(Yhat[0:5])