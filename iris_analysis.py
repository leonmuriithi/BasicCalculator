import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df["species"] = pd.Categorical.from_codes(iris.target, iris.target_names)

print(df.head())
print(df.info())
print(df.isnull().sum())

print(df.describe())
grouped = df.groupby("species").mean()
print(grouped[["petal length (cm)"]])

df["index"] = df.index
plt.plot(df["index"], df["sepal length (cm)"])
plt.title("Sepal Length Over Time")
plt.xlabel("Index")
plt.ylabel("Sepal Length (cm)")
plt.grid(True)
plt.show()

sns.barplot(x=grouped.index, y=grouped["petal length (cm)"])
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()

df["sepal width (cm)"].hist(bins=10)
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

sns.scatterplot(data=df, x="sepal length (cm)", y="petal length (cm)", hue="species")
plt.title("Sepal vs Petal Length by Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.show()