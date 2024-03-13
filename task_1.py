import networkx as nx
import matplotlib.pyplot as plt


def create_graph():
    # Create road system graph
    G = nx.Graph()
    # A, B, ... - Vertices
    # weight - Edge weight
    edges = [('A', 'B', {'weight': 5}),
             ('A', 'C', {'weight': 7}),
             ('B', 'C', {'weight': 3}),
             ('B', 'D', {'weight': 8}),
             ('C', 'D', {'weight': 6}),
             ('C', 'E', {'weight': 4}),
             ('D', 'E', {'weight': 9}),
             ('D', 'F', {'weight': 2}),
             ('E', 'F', {'weight': 5})]
    G.add_edges_from(edges)
    return G


def main():
    G = create_graph()
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=1000,
            node_color='skyblue', font_size=12, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, font_color='red', font_size=10, edge_labels={
        (u, v): d['weight'] for u, v, d in G.edges(data=True)})
    plt.title('Road system')
    plt.show()

    # Аналіз характеристик графа
    print("Vertices count:", G.number_of_nodes())
    print("Edges count:", G.number_of_edges())
    print("Vertices degree:", dict(G.degree()))


if __name__ == '__main__':
    main()
