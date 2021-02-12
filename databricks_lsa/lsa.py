red = open("littleredridinghood.txt").read().splitlines()
gold = open("goldilocks.txt").read().splitlines()

# create body data frame
import pandas as pd

red_df = pd.DataFrame({"title": "LittleRedRidingHood", "sentence": red})
gold_df = pd.DataFrame({"title": "Goldilocks", "sentence": gold})

body_df = pd.concat([red_df, gold_df], ignore_index=True)

# create document-term matrix
#from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

vectoriser = TfidfVectorizer(min_df=1, stop_words="english")
bag_of_words = vectoriser.fit_transform(body_df.sentence)

# perform singular value decomposition
from sklearn.decomposition import TruncatedSVD

svd = TruncatedSVD(n_components=2)
lsa = svd.fit_transform(bag_of_words)

# topic encoded data
topic_encoded_df = pd.DataFrame(lsa, columns = ["topic_1", "topic_2"])
topic_encoded_df["sentence"] = body_df.sentence
topic_encoded_df["isRedRidingHood"] = (body_df.title == "LittleRedRidingHood")

# dictionary
dictionary = vectoriser.get_feature_names()

# encoding matrix
encoding_matrix = pd.DataFrame(svd.components_, index=["topic_1", "topic_2"]).T
encoding_matrix["terms"] = dictionary

# interpret encoding matrix
import numpy as np

encoding_matrix["abs_topic_1"] = np.abs(encoding_matrix["topic_1"])
encoding_matrix["abs_topic_2"] = np.abs(encoding_matrix["topic_2"])

print(encoding_matrix.sort_values("abs_topic_1", ascending=False))
print(encoding_matrix.sort_values("abs_topic_2", ascending=False))

# plot topic encoded data
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

for val in topic_encoded_df.isRedRidingHood.unique():
    topic_1 = topic_encoded_df[topic_encoded_df.isRedRidingHood == val]["topic_1"].values
    topic_2 = topic_encoded_df[topic_encoded_df.isRedRidingHood == val]["topic_2"].values
    colour = "red" if val else "green"
    label = "LittleRedRidingHood" if val else "Goldilocks"
    ax.scatter(topic_1, topic_2, c=colour, alpha=0.3, label=label)

ax.set_xlabel("First Topic")
ax.set_ylabel("Second Topic")
ax.axvline(linewidth=0.5)
ax.axhline(linewidth=0.5)
ax.legend()

fig.show()
