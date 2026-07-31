# import pandas as pd




# def preprocess_dataset(nodes_file, edges_file):

#     nodes = pd.read_csv(nodes_file)
#     edges = pd.read_csv(edges_file)

#     original_nodes = len(nodes)
#     original_edges = len(edges)

#     # Remove duplicate nodes
#     nodes = nodes.drop_duplicates()
#     duplicate_nodes = original_nodes - len(nodes)

#     # Remove duplicate edges
#     edges = edges.drop_duplicates()
#     duplicate_edges = original_edges - len(edges)

#     # Missing values
#     missing_nodes = nodes.isnull().sum().sum()
#     missing_edges = edges.isnull().sum().sum()

#     nodes = nodes.dropna()
#     edges = edges.dropna()

#     # Invalid Node IDs
#     valid_nodes = set(nodes["NodeID"])

#     invalid_edges = edges[
#         (~edges["SourceNode"].isin(valid_nodes)) |
#         (~edges["TargetNode"].isin(valid_nodes))
#     ]

#     invalid_count = len(invalid_edges)

#     edges = edges[
#         edges["SourceNode"].isin(valid_nodes) &
#         edges["TargetNode"].isin(valid_nodes)
#     ]

#     # Remove self loops
#     self_loops = len(
#         edges[
#             edges["SourceNode"] == edges["TargetNode"]
#         ]
#     )

#     edges = edges[
#         edges["SourceNode"] != edges["TargetNode"]
#     ]

#     return {

#         "nodes": nodes,
#         "edges": edges,

#         "duplicate_nodes": duplicate_nodes,
#         "duplicate_edges": duplicate_edges,

#         "missing_nodes": missing_nodes,
#         "missing_edges": missing_edges,

#         "invalid_edges": invalid_count,

#         "self_loops": self_loops,

#         "graph_ready": True

#     }

import pandas as pd


def preprocess_dataset(nodes_file, edges_file):

    nodes = pd.read_csv(nodes_file)
    edges = pd.read_csv(edges_file)

    # Remove extra spaces from column names
    nodes.columns = nodes.columns.str.strip()
    edges.columns = edges.columns.str.strip()

    # -------- Detect Node ID column --------
    if "NodeID" in nodes.columns:
        node_col = "NodeID"
    elif "nodeid" in nodes.columns:
        node_col = "nodeid"
    elif "ID" in nodes.columns:
        node_col = "ID"
    elif "id" in nodes.columns:
        node_col = "id"
    else:
        raise ValueError(
            f"Node ID column not found. Available columns: {list(nodes.columns)}"
        )

    # -------- Detect Source column --------
    if "SourceNode" in edges.columns:
        source_col = "SourceNode"
    elif "Source" in edges.columns:
        source_col = "Source"
    elif "source" in edges.columns:
        source_col = "source"
    else:
        raise ValueError(
            f"Source column not found. Available columns: {list(edges.columns)}"
        )

    # -------- Detect Target column --------
    if "TargetNode" in edges.columns:
        target_col = "TargetNode"
    elif "Target" in edges.columns:
        target_col = "Target"
    elif "target" in edges.columns:
        target_col = "target"
    else:
        raise ValueError(
            f"Target column not found. Available columns: {list(edges.columns)}"
        )

    original_nodes = len(nodes)
    original_edges = len(edges)

    nodes = nodes.drop_duplicates()
    edges = edges.drop_duplicates()

    duplicate_nodes = original_nodes - len(nodes)
    duplicate_edges = original_edges - len(edges)

    missing_nodes = nodes.isnull().sum().sum()
    missing_edges = edges.isnull().sum().sum()

    nodes = nodes.dropna()
    edges = edges.dropna()

    valid_nodes = set(nodes[node_col])

    invalid_edges = edges[
        (~edges[source_col].isin(valid_nodes)) |
        (~edges[target_col].isin(valid_nodes))
    ]

    invalid_count = len(invalid_edges)

    edges = edges[
        edges[source_col].isin(valid_nodes) &
        edges[target_col].isin(valid_nodes)
    ]

    self_loops = len(
        edges[
            edges[source_col] == edges[target_col]
        ]
    )

    edges = edges[
        edges[source_col] != edges[target_col]
    ]

    return {
        "nodes": nodes,
        "edges": edges,
        "duplicate_nodes": duplicate_nodes,
        "duplicate_edges": duplicate_edges,
        "missing_nodes": missing_nodes,
        "missing_edges": missing_edges,
        "invalid_edges": invalid_count,
        "self_loops": self_loops,
        "graph_ready": True,
    }