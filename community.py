import networkx as nx
import pandas as pd

import community.community_louvain as community_louvain

from sklearn.cluster import SpectralClustering
from sklearn.cluster import KMeans
from sklearn.decomposition import TruncatedSVD


def load_graph(edge_file):

    edges = pd.read_csv(edge_file)

    G = nx.Graph()

    for _, row in edges.iterrows():

        G.add_edge(

            row["SourceNode"],
            row["TargetNode"]

        )

    return G


# -------------------------------
# Louvain Algorithm
# -------------------------------

def louvain_detection(edge_file):

    G = load_graph(edge_file)

    partition = community_louvain.best_partition(G)

    return G, partition


# -------------------------------
# Spectral Clustering
# -------------------------------

def spectral_detection(edge_file, clusters=5):

    G = load_graph(edge_file)

    adjacency_matrix = nx.to_numpy_array(G)

    model = SpectralClustering(

        n_clusters=clusters,

        affinity="precomputed",

        random_state=42

    )

    labels = model.fit_predict(adjacency_matrix)

    communities = {}

    for node, label in zip(G.nodes(), labels):

        communities[node] = int(label)

    return G, communities


# -------------------------------
# K-Means Clustering
# -------------------------------

def kmeans_detection(edge_file, clusters=5):

    G = load_graph(edge_file)

    adjacency_matrix = nx.to_numpy_array(G)

    # Convert graph to embedding space
    svd = TruncatedSVD(

        n_components=10,

        random_state=42

    )

    embeddings = svd.fit_transform(adjacency_matrix)

    model = KMeans(

        n_clusters=clusters,

        random_state=42,

        n_init="auto"

    )

    labels = model.fit_predict(embeddings)

    communities = {}

    for node, label in zip(G.nodes(), labels):

        communities[node] = int(label)

    return G, communities


# -------------------------------
# Common Function
# -------------------------------

def detect_communities(node_file, edge_file, algorithm="louvain"):

    if algorithm == "spectral":

        G, communities = spectral_detection(edge_file)

    elif algorithm == "kmeans":

        G, communities = kmeans_detection(edge_file)

    else:

        G, communities = louvain_detection(edge_file)

    return communities

# import networkx as nx
# import pandas as pd

# import community.community_louvain as community_louvain
# from community_detection_ml.community import detect_communities
# from sklearn.cluster import SpectralClustering

# def load_graph(edge_file):

#     edges = pd.read_csv(edge_file)

#     G = nx.Graph()

#     for _, row in edges.iterrows():

#         G.add_edge(

#             row["SourceNode"],
#             row["TargetNode"]

#         )

#     return G

# def louvain_detection(edge_file):

#     G = load_graph(edge_file)

#     partition = community_louvain.best_partition(G)

#     return G, partition

# def spectral_detection(edge_file, clusters=5):

#     G = load_graph(edge_file)

#     A = nx.to_numpy_array(G)

#     model = SpectralClustering(

#         n_clusters=clusters,

#         affinity="precomputed",

#         random_state=42

#     )

#     labels = model.fit_predict(A)

#     result = {}

#     for node, label in zip(G.nodes(), labels):

#         result[node] = int(label)

#     return G, result

# def detect_communities(node_file, edge_file):

#     G, communities = louvain_detection(edge_file)

#     return communities