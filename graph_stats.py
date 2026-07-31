# import pandas as pd
# import networkx as nx


# def calculate_statistics(edge_file):

#     edges = pd.read_csv(edge_file)

#     G = nx.Graph()

#     for _, row in edges.iterrows():

#         G.add_edge(

#             row["SourceNode"],
#             row["TargetNode"]

#         )

#     statistics = {

#         "total_nodes": G.number_of_nodes(),

#         "total_edges": G.number_of_edges(),

#         "density": round(
#             nx.density(G),
#             4
#         ),

#         "connected_components":

#         nx.number_connected_components(G),

#         "average_degree":

#         round(

#             sum(dict(G.degree()).values())

#             / G.number_of_nodes(),

#             2

#         ),

#         "average_clustering":

#         round(

#             nx.average_clustering(G),

#             4

#         )

#     }

#     return statistics

import pandas as pd
import networkx as nx


def calculate_statistics(edge_file):
    # Read CSV
    edges = pd.read_csv(edge_file)

    # Remove spaces from column names
    edges.columns = edges.columns.str.strip()

    # Validate required columns
    required_columns = ["SourceNode", "TargetNode"]

    for col in required_columns:
        if col not in edges.columns:
            raise ValueError(
                f"Column '{col}' not found.\n"
                f"Available columns: {list(edges.columns)}"
            )

    # Create Graph
    G = nx.Graph()

    for _, row in edges.iterrows():
        G.add_edge(row["SourceNode"], row["TargetNode"])

    degree_dict = dict(G.degree())

    total_nodes = G.number_of_nodes()
    total_edges = G.number_of_edges()

    if total_nodes == 0:
        return {}

    statistics = {
        "total_nodes": total_nodes,
        "total_edges": total_edges,
        "density": round(nx.density(G), 4),
        "average_degree": round(sum(degree_dict.values()) / total_nodes, 2),
        "maximum_degree": max(degree_dict.values()),
        "minimum_degree": min(degree_dict.values()),
        "average_clustering": round(nx.average_clustering(G), 4),
        "connected_components": nx.number_connected_components(G),
        "largest_component": len(max(nx.connected_components(G), key=len)),
        "graph_type": "Undirected"
    }

    return statistics