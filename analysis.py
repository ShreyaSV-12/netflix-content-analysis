import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("netflix_titles.csv")

content_type = df["type"].value_counts()

plt.figure(figsize=(6,4))
content_type.plot(kind="bar")

plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Content Type")
plt.ylabel("Count")

plt.tight_layout()
plt.savefig("movies_vs_tvshows.png")
plt.show()
