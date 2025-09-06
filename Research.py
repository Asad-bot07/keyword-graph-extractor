import networkx as nx
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
import string
import re
text = """
Continuing their drive against child marriage, officials in Perambalur district have rescued seven more under-aged girls over the past week.

While four marriages that were scheduled over the last week were stopped by the officials, three others who were already given in marriage were rescued and handed over to the Childline in Tiruchi.

Of the marriages, three were to be held on Thursday and another on Saturday.

Acting on information from village level committees and the public, officials of the Social Welfare and Revenue departments visited the households of the brides to stop the marriages.

One of the four brides was a 13-year-old; two others were 16 and another was 17.

Three of the marriages that were stopped were in Kunnam taluk for girls hailing from Thungapuram, Kadur and Labbaikudikadu.

Another marriage was stopped at Somandapudur in Perambalur taluk.

District Social Welfare Officer K. Petchiammal said that interim injunctions against the conduct of the marriages were obtained from the Judicial Magistrate in all the four cases so that the parents did not go ahead with the marriage.

Three other girls below the age of 18 from Melamathur, Kolakanatham and Paravai villages, who were married recently, were rescued and handed over to the Childline in Tiruchi.

Rehabilitation measures

The girls would be produced before the Child Welfare Committee, which would decide on rehabilitation measures.

Admission to schools

Ms. Petchiammal said steps would be taken for admitting the girls into schools, depending upon their willingness.

Since July, about 15 girls were rescued from child marriages in the district.
"""
tokens = re.findall(r'\b[a-zA-Z]{2,}\b', text.lower())
tokens = [t for t in tokens if t not in ENGLISH_STOP_WORDS]
window_size = 2
G = nx.Graph()
for i in range(len(tokens) - window_size + 1):
    window = tokens[i:i + window_size]
    for i in range(len(window)):
        for j in range(i + 1, len(window)):
            w1, w2 = window[i], window[j]
            if G.has_edge(w1, w2):
                G[w1][w2]['weight'] += 1
            else:
                G.add_edge(w1, w2, weight=1)
ranks = nx.pagerank(G)
top_keywords = sorted(ranks.items(), key=lambda x: x[1], reverse=True)[:10]
print("\nTop Keywords:")
for word, score in top_keywords:
    print(f"{word}: {score:.4f}")
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, k=.5, seed=42)
nx.draw_networkx_nodes(G, pos, node_color='pink', node_size=1800)
nx.draw_networkx_edges(G, pos, edge_color='black')
nx.draw_networkx_labels(G, pos, font_size=8)
plt.title("Word Co-occurrence Graph", fontsize=14)
plt.axis('off')
plt.tight_layout()
plt.savefig("word_graph_302.png")
plt.show()