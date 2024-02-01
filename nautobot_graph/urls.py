from django.urls import path


from nautobot.apps.urls import NautobotUIViewSetRouter
from nautobot.apps.views import ObjectDynamicGroupsView

from nautobot_graph import views
from nautobot_graph.models import (
    NodeLabel,
    NodeProperty,
    NodeType,
    RelationshipProperty,
    RelationshipType,
)


app_name = "nautobot_graph"
router = NautobotUIViewSetRouter()


router.register("node-labels", views.NodeLabelModelUIViewSet)
router.register("node-properties", views.NodePropertyModelUIViewSet)
router.register("node-types", views.NodeTypeModelUIViewSet)
router.register("relationship-properties", views.RelationshipPropertyModelUIViewSet)
router.register("relationship-types", views.RelationshipTypeModelUIViewSet)


urlpatterns = [
    path("", views.NautobotGraphHomeView.as_view(), name="home"),
    path(
        "node-labels/<uuid:pk>/dynamic-groups/",
        ObjectDynamicGroupsView.as_view(),
        name="nodelabel_dynamicgroups",
        kwargs={"node-label": NodeLabel},
    ),
    path(
        "node-labels/<uuid:pk>/dynamic-groups/",
        ObjectDynamicGroupsView.as_view(),
        name="nodeproperty_dynamicgroups",
        kwargs={"node-properties": NodeProperty},
    ),
    path(
        "node-types/<uuid:pk>/dynamic-groups/",
        ObjectDynamicGroupsView.as_view(),
        name="nodetype_dynamicgroups",
        kwargs={"node-types": NodeType},
    ),
    path(
        "relationship-properties/<uuid:pk>/dynamic-groups/",
        ObjectDynamicGroupsView.as_view(),
        name="relationshipproperty_dynamicgroups",
        kwargs={"relationship-properties": RelationshipProperty},
    ),
    path(
        "relationship-types/<uuid:pk>/dynamic-groups/",
        ObjectDynamicGroupsView.as_view(),
        name="relationshiptype_dynamicgroups",
        kwargs={"relationship-types": RelationshipType},
    ),
]
urlpatterns += router.urls
