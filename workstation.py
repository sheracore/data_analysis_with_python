import pandas as pd

df = pd.read_csv("csv_sample.csv")
df = pd.read_csv("csv_sample.csv", header = None)
print(df.head(10))
print(df.tail(10))
print(df.columns)
df = pd.read_csv("csv_sample.csv")
print(df.columns)
df.to_csv("output.csv")
#--------------------------------------

print("***********", df.dtypes) # ==> type of all columns
print(df.describe()) # ==> returns a statistical summary
print(df.describe(include="all")) # ==> returns full statistical summary
#Some of this data is NaN its because that particular statistical metric cannot be calculated for that specific
print(df.info()) # ==> provides a concise summary of you DataFrame
df["PAGING_INTENSITY(PPS/CELL)"] = df["PAGING_INTENSITY(PPS/CELL)"].astype("float")

# To normalization between 0 and 1
#df["PAGING_INTENSITY(PPS/CELL)"] = df["PAGING_INTENSITY(PPS/CELL)"]/df["PAGING_INTENSITY(PPS/CELL)"].max()
#df["PAGING_INTENSITY(PPS/CELL)"] = (df["PAGING_INTENSITY(PPS/CELL)"]-df["PAGING_INTENSITY(PPS/CELL)"].min())/(df["PAGING_INTENSITY(PPS/CELL)"].max()-df["PAGING_INTENSITY(PPS/CELL)"].min())

#df["PAGING_INTENSITY(PPS/CELL)"] = (df["PAGING_INTENSITY(PPS/CELL)"]-df["PAGING_INTENSITY(PPS/CELL)"].mean())/df["PAGING_INTENSITY(PPS/CELL)"].std()

binwidth = int(((int(max(df["RAB_EST_SR_CS"]))-int(min(df["RAB_EST_SR_CS"])))/4))
bins = range(int(min(df["RAB_EST_SR_CS"])), int(max(df["RAB_EST_SR_CS"])) , binwidth)
print(binwidth,bins)
group_names = ['Low', 'Lo_Med' ,'Medium', 'Med_to_Hight' , 'High']
df['range'] = pd.cut(df['RAB_EST_SR_CS'], bins, labels=group_names)
print(df['RAB_EST_SR_CS'], df['range'] )

print(bins)

print(pd.get_dummies(df['REGION']))
df_region_dummy = pd.get_dummies(df['REGION'])
print(df_region_dummy['R1'].std())

print(df['REGION'].value_counts())

#df_test = df['drive_wheels', 'body_style', 'price']
#df_grp = df_test.groupby(['drive_wheels', 'body_style'], as_index=False).mean()

import seaborn as sns
import matplotlib.pyplot as plt

sns.regplot(x="RAB_EST_SR_CS", y="DROP_CALL_RATE", data=df)
plt.ylim(0,)
