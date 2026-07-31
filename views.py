from django.shortcuts import render
from upload.models import Dataset

import pandas as pd

from community_detection_ml.community import detect_communities
from .visualization import visualize_graph
from community_detection_ml.community import louvain_detection

def visualization(request):

    dataset = Dataset.objects.last()

    if dataset is None:

        return render(

            request,

            "visualization.html",

            {

                "error":"Upload Dataset First"

            }

        )

    nodes = pd.read_csv(

        dataset.node_file.path

    )

    edges = pd.read_csv(

        dataset.edge_file.path

    )

    communities = detect_communities(

        dataset.node_file.path,

        dataset.edge_file.path

    )

    image = visualize_graph(

        nodes,

        edges,

        communities

    )

    return render(

        request,

        "visualization.html",

        {

            "image":"visualization/graph.png"

        }

    )
# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required

# @login_required
# def visualization(request):

#     return render(request, "visualization.html")