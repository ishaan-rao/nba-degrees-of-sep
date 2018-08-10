import networkx as nx

edges = open("player_edges.csv", 'rb')

G = nx.read_edgelist(edges, delimiter=",")


def shortest_path(player1, player2):
    return nx.shortest_path(G, player1, player2)

def all_shortest_paths(player1, player2):
    return list(nx.all_shortest_paths(G, player1, player2))

def deg_of_sep(player1, player2):
    return len(nx.shortest_path(G, player1, player2))

# count = 0
# for node in sorted(G.degree, key=lambda x: x[1], reverse=True):
#     if (count < 20):
#         print(node)
#     count += 1

edges.close()
