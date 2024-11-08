import pandas as pd





df=pd.read_csv('avgIQpercountry.csv')
#print(df.info())

subset=df[["Country","Average IQ"]]
filtered_df=subset[subset["Average IQ"]>100]
print(filtered_df)

null_mask=df.isnull()
null_count=null_mask.sum()
print(f"null count:{null_count}")

duplicated_count=df.duplicated().sum()

print(f"duplicated count:{duplicated_count}")
df.drop_duplicates(keep='first', inplace=True)
ave_iq_per_country=df.groupby("Country")["Average IQ"].mean()
print(ave_iq_per_country.sort_values(ascending=False))







