import pandas as pd
import matplotlib as plt

df=pd.read_csv("weather_tokyo_date.csv")
print(df.info())
df['temperature']=pd.to_numeric(df['temperature'], errors='coerce')
avgTemperature=df["temperature"].mean()
roundavgTemperature=round(avgTemperature,2)
print(f"This is the temperature asked on question 1 {roundavgTemperature}")


df["month"]=df["day"].dt.month

monthly_avg_temperature=df.groupby("month")["temperature"].mean().round(2)
print(f"This is the temperature asked on question 2:{monthly_avg_temperature}")

monthly_avg_temperature.plot(kind='bar',color="pink")
plt.title("Average Temperature")
plt.xlabel("Monthly Average Temperature")
plt.ylabel("Temperature")
plt.show()

hottest_day=df.loc[df['temperature'].]


