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

print(df.dtypes) # ==> type of all columns
print(df.describe()) # ==> returns a statistical summary
print(df.describe(include="all")) # ==> returns full statistical summary
#Some of this data is NaN its because that particular statistical metric cannot be calculated for that specific
print(df.info()) # ==> provides a concise summary of you DataFrame
df["PAGING_INTENSITY(PPS/CELL)"] = df["PAGING_INTENSITY(PPS/CELL)"].astype("float")

# To normalization between 0 and 1
df["PAGING_INTENSITY(PPS/CELL)"] = df["PAGING_INTENSITY(PPS/CELL)"]/df["PAGING_INTENSITY(PPS/CELL)"].max()
df["PAGING_INTENSITY(PPS/CELL)"] = (df["PAGING_INTENSITY(PPS/CELL)"]-df["PAGING_INTENSITY(PPS/CELL)"].min())/(df["PAGING_INTENSITY(PPS/CELL)"].max()-df["PAGING_INTENSITY(PPS/CELL)"].min())

df["PAGING_INTENSITY(PPS/CELL)"] = (df["PAGING_INTENSITY(PPS/CELL)"]-df["PAGING_INTENSITY(PPS/CELL)"].mean())/df["PAGING_INTENSITY(PPS/CELL)"].std()
