import os
import random
import networkx as nx
import matplotlib.pyplot as plt


def visualize_graph(nodes_df, edges_df, communities):

    G = nx.Graph()

    # Add nodes
    for _, row in nodes_df.iterrows():
        G.add_node(row["NodeID"])

    # Add edges
    for _, row in edges_df.iterrows():
        G.add_edge(
            row["SourceNode"],
            row["TargetNode"]
        )

    # Random color for each community
    colors = {}

    for c in set(communities.values()):

        colors[c] = (
            random.random(),
            random.random(),
            random.random()
        )

    node_colors = []

    for node in G.nodes():

        community = communities.get(node, 0)

        node_colors.append(
            colors[community]
        )

    plt.figure(figsize=(12,8))

    pos = nx.spring_layout(
        G,
        seed=42
    )

    nx.draw_networkx(

        G,

        pos,

        node_size=180,

        node_color=node_colors,

        edge_color="gray",

        with_labels=False

    )

    folder = "static/visualization"

    os.makedirs(
        folder,
        exist_ok=True
    )

    output = os.path.join(
        folder,
        "graph.png"
    )

    plt.savefig(
        output,
        dpi=250,
        bbox_inches="tight"
    )

    plt.close()

    return output