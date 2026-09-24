import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("marketing_campaign.csv", sep="\t")
df["Dt_Customer"] = pd.to_datetime(df["Dt_Customer"], dayfirst=True, errors="coerce")
df["Income"] = pd.to_numeric(df["Income"], errors="coerce")

product_cols = ["MntWines","MntFruits","MntMeatProducts","MntFishProducts","MntSweetProducts","MntGoldProds"]
channel_cols = ["NumWebPurchases","NumCatalogPurchases","NumStorePurchases"]
campaign_cols = [f"AcceptedCmp{i}" for i in range(1,6)]

df["TotalSpend"] = df[product_cols].sum(axis=1)
df["TotalPurchases"] = df[channel_cols].sum(axis=1)
df["TotalCampaignAccepted"] = df[campaign_cols].sum(axis=1)
df["Children"] = df["Kidhome"] + df["Teenhome"]
df["Age_2014"] = 2014 - df["Year_Birth"]
df["RecencyBand"] = pd.cut(df["Recency"], [-1,30,60,90,120],
                           labels=["0-30","31-60","61-90","91-120"])

# Basic EDA
print("Shape:", df.shape)
print("\nMissing values:\n", df.isna().sum().sort_values(ascending=False).head(10))
print("\nDuplicate rows:", df.duplicated().sum())
print("\nDescriptive statistics:\n", df.describe(include="all").T)

# KPI summary
print("\nResponse rate:", round(df.Response.mean()*100,2), "%")
print("Complaint rate:", round(df.Complain.mean()*100,2), "%")
print("Average spend:", round(df.TotalSpend.mean(),2))
print("Median spend:", round(df.TotalSpend.median(),2))

# Segments
print("\nEducation:")
print(df.groupby("Education").agg(Customers=("ID","count"),
    AvgIncome=("Income","mean"), AvgSpend=("TotalSpend","mean"),
    ResponseRate=("Response","mean")).sort_values("AvgSpend", ascending=False))

print("\nRecency:")
print(df.groupby("RecencyBand", observed=False).agg(Customers=("ID","count"),
    AvgSpend=("TotalSpend","mean"), ResponseRate=("Response","mean")))

# Visualizations
plt.figure(figsize=(9,5)); plt.hist(df.TotalSpend.dropna(), bins=40)
plt.title("Customer Total Spend Distribution"); plt.xlabel("Total spend"); plt.ylabel("Customers"); plt.show()

plt.figure(figsize=(9,5)); s=df[product_cols].sum().sort_values()
plt.barh([x.replace("Mnt","") for x in s.index], s.values)
plt.title("Revenue Contribution by Product Category"); plt.xlabel("Recorded product spend"); plt.show()

plt.figure(figsize=(8,5)); c=df[channel_cols].sum()
plt.bar(["Web","Catalog","Store"], [c["NumWebPurchases"],c["NumCatalogPurchases"],c["NumStorePurchases"]])
plt.title("Purchase Volume by Channel"); plt.ylabel("Purchases"); plt.show()

plt.figure(figsize=(8,5)); r=df.groupby("RecencyBand", observed=False).Response.mean()*100
plt.plot(r.index.astype(str), r.values, marker="o")
plt.title("Campaign Response Rate by Recency"); plt.xlabel("Recency band"); plt.ylabel("Response rate (%)"); plt.show()

plt.figure(figsize=(8,6))
p=df[["Income","TotalSpend","Response"]].dropna()
for v,m in [(0,"o"),(1,"x")]:
    q=p[p.Response==v]; plt.scatter(q.Income,q.TotalSpend,alpha=.45,marker=m,label=f"Response={v}")
plt.title("Income vs Total Spend"); plt.xlabel("Income"); plt.ylabel("Total spend"); plt.legend(); plt.show()

corr=df[["Income","Recency","TotalSpend","NumWebPurchases","NumCatalogPurchases","NumStorePurchases","NumWebVisitsMonth","Response"]].corr()
plt.figure(figsize=(9,7)); plt.imshow(corr,aspect="auto"); plt.colorbar(label="Correlation")
plt.xticks(range(len(corr)),corr.columns,rotation=45,ha="right"); plt.yticks(range(len(corr)),corr.columns)
for i in range(len(corr)):
    for j in range(len(corr)): plt.text(j,i,f"{corr.iloc[i,j]:.2f}",ha="center",va="center",fontsize=8)
plt.title("Correlation Heatmap"); plt.show()
