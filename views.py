# from django.shortcuts import render

# # Create your views here.
# from django.shortcuts import render

# from upload.models import Dataset

# from .community import *

# def detect_community(request):

#     dataset = Dataset.objects.last()

#     if dataset is None:

#         return render(

#             request,

#             "community_detection.html",

#             {

#                 "error":"Upload Dataset First"

#             }

#         )

#     algorithm = request.GET.get(

#         "algorithm",

#         "louvain"

#     )

#     if algorithm=="spectral":

#         G, communities = spectral_detection(

#             dataset.edge_file.path

#         )

#     else:

#         G, communities = louvain_detection(

#             dataset.edge_file.path

#         )

#     total_nodes = G.number_of_nodes()

#     total_edges = G.number_of_edges()

#     total_communities = len(

#         set(

#             communities.values()

#         )

#     )

#     context={

#         "algorithm":algorithm,

#         "nodes":total_nodes,

#         "edges":total_edges,

#         "communities":total_communities,

#         "results":list(communities.items())[:20]

#     }

#     return render(

#         request,

#         "community_detection.html",

#         context

#     )

from django.shortcuts import render
from upload.models import Dataset

from .community import (
    louvain_detection,
    spectral_detection,
    kmeans_detection
)


def detect_community(request):

    dataset = Dataset.objects.last()

    if dataset is None:

        return render(

            request,

            "community_detection.html",

            {

                "error": "Upload Dataset First"

            }

        )

    algorithm = request.GET.get(

        "algorithm",

        "louvain"

    )

    if algorithm == "spectral":

        G, communities = spectral_detection(

            dataset.edge_file.path

        )

    elif algorithm == "kmeans":

        G, communities = kmeans_detection(

            dataset.edge_file.path

        )

    else:

        G, communities = louvain_detection(

            dataset.edge_file.path

        )

    context = {

        "algorithm": algorithm,

        "nodes": G.number_of_nodes(),

        "edges": G.number_of_edges(),

        "communities": len(set(communities.values())),

        "results": list(communities.items())[:20]

    }

    return render(

        request,

        "community_detection.html",

        context

    )