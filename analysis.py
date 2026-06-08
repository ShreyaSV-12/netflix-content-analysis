import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("netflix_titles.csv")

top_years = df["release_year"].value_counts().head(10)

top_years.plot(kind="bar")

plt.title("Top 10 Release Years on Netflix")
plt.xlabel("Year")
plt.ylabel("Number of Titles")

plt.tight_layout()
plt.savefig("netflix_release_years.png")
plt.show()
