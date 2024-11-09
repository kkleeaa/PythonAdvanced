import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('avgIQpercountry.csv')
filtered=df[df["Average IQ"]>100]
filtered=filtered.sort_values(by=['Average IQ'],ascending=False)
print(filtered)

plt.figure(figsize=(14,8))

bars=plt.bar(filtered["Country"], filtered["Average IQ"],color="pink")
plt.title("Average IQ per country")


plt.xlabel("Country")
plt.ylabel("Average IQ")
plt.xticks(rotation=90,fontsize=14)
plt.yticks(fontsize=14)

plt.grid(axis="y",linestyle="--", alpha=0.8)

plt.bar_label(bars,fnt="%.2f", fontsize=10,color="green")
plt.tight_layout()
plt.show()


