import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedKFold
from sklearn.preprocessing import MinMaxScaler


#load the data
df = pd.read_csv("instagram_reach.csv")

df.head()

df.info()

#first take backup of the dataset
df_backup = df.copy()
df_backup.head()


#drop columns
df.drop(columns=['Unnamed: 0', 'S.No', 'USERNAME'], inplace = True)

df['Time since posted'] = df['Time since posted'].map(lambda a: int(re.sub('hours', '', a)))


df.describe()


df.isnull().sum()



#droping the null values since they are unlikley to effect the target variables
df.dropna()


cols = ['Followers', 'Time since posted', 'Likes']


def get_histplot(col):
    ax = sns.kdeplot(df[col])
    Q1 = np.percentile(df[col],25)
    Q3 = np.percentile(df[col],75)
    IQR=Q3-Q1    
    lower_threshold = Q1 - 1.5*IQR
    upper_threshold = Q3 + 1.5*IQR
    
    ax.axvline(Q1, color='red', linestyle='-', label="Q1")
    ax.axvline(Q3, color='blue', linestyle='-', label="Q3")
    ax.axvline(lower_threshold, color='yellow', linestyle='-', label="Lower threshold")
    ax.axvline(upper_threshold, color='green', linestyle='-', label="Upper threshold")
    ax.legend()
for i in cols:
    get_histplot(i)
    plt.show()
    

# create box plots
fig, ax = plt.subplots(ncols=3, nrows=1, figsize=(10,4))
index = 0
ax = ax.flatten()

for col in cols:
    sns.boxplot(y=col, data=df, ax=ax[index], color='r')
    plt.subplots_adjust(wspace = .5)
    index += 1
    plt.show()

sns.lmplot(x='Time since posted', y='Likes', data=df, fit_reg=True)

plt.title('Likes vs Times since posted ')
plt.xlabel('Times since posted (hours)')
plt.ylabel('Likes')
plt.show()

sns.lmplot(x='Followers', y='Likes', data=df, fit_reg=True)

plt.title('Likes vs Followers')
plt.xlabel('Followers')
plt.ylabel('Likes')
plt.show()

scaler = MinMaxScaler()
df[['Followers', 'Time since posted']] = scaler.fit_transform(df[['Followers', 'Time since posted']])


#Define x variables and y variable
x = df[['Followers', 'Time since posted']]
y = df['Likes']

#Split train set and test set
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)


from xgboost import XGBRegressor
model = XGBRegressor()
model.fit(X_train, y_train)

from numpy import absolute
cv = RepeatedKFold(n_splits=10, n_repeats=5, random_state=1)
#Evaluate the model
scores = cross_val_score(model, X_test, y_test, scoring='neg_mean_absolute_error', cv=cv, n_jobs=-1)
#Absolute MAE
scores = absolute(scores)
print('Mean MAE: %.3f (%.3f)' % (scores.mean(), scores.std()))





