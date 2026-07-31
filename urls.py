from django.contrib import admin
from django.urls import path
from django.urls import include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path(
        "admin/",
        admin.site.urls
    ),

    path(
        "",
        include("accounts.urls")
    ),
    path(

    "upload/",

    include("upload.urls")

    ),
    path("",include("preprocessing.urls")),
    path(
    "graph/",
    include("graph.urls")
),
path(
    "community/",
    include("community_detection_ml.urls")
),
path(
    "visualization/",
    include("visualization.urls")
),
path(

    "graph_statistics/",

    include("graph_statistics.urls")

),
path(

    "embeddings/",

    include("embeddings.urls")

),
path(
    "evaluation/",
    include("evaluation.urls")
),
path(
    "report/",
    include("report.urls")
),
]

# Serve uploaded media files
if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

   