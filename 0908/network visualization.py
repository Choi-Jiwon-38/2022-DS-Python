import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

# G.add_node("A")
# G.add_node("B")
G.add_edge("A", "B")

pos = {"A": (1,1), "B": (0,0)} # 노드를 랜덤한 위치(기본)이 아닌 고정하여 출력하고 싶은 경우

nx.draw(G, pos, with_labels = True)
plt.show()