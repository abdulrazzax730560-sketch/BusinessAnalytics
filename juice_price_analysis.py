import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Price": [20, 25, 30, 35, 40],
    "Bottles_Sold": [120, 110, 90, 80, 70]
}
df = pd.DataFrame(data)

print("Original Dataset:")
print(df)
print()

df["Revenue"] = df["Price"] * df["Bottles_Sold"]

print("Updated Dataset with Revenue:")
print(df)
print()

max_revenue = df["Revenue"].max()
best_price = df.loc[df["Revenue"].idxmax(), "Price"]

print(f"Highest Revenue: ₹{max_revenue}")
print(f"Price that generated the highest revenue: ₹{best_price}")
print()

plt.figure(figsize=(8, 5))
bars = plt.bar(df["Price"].astype(str), df["Revenue"], color="skyblue", edgecolor="black")

best_index = df["Revenue"].idxmax()
bars[best_index].set_color("orange")

plt.title("Price vs Revenue - Juice Shop Analysis")
plt.xlabel("Price (₹)")
plt.ylabel("Revenue (₹)")
plt.tight_layout()
plt.savefig("price_vs_revenue.png", dpi=150)
plt.show()

print("Conclusion:")
print(f"The shop owner should set the price at ₹{best_price} per bottle, since it generates the "
      f"highest revenue of ₹{max_revenue} among all tested prices (₹40 ties at the same revenue, "
      f"but ₹{best_price} sells more bottles for the same earnings). Although higher prices reduce "
      f"the number of bottles sold, ₹{best_price} strikes the best balance between price and demand, "
      f"maximizing overall revenue while moving more product than ₹40 would.")
