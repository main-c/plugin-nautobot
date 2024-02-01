from nautobot.apps.ui import HomePageItem, HomePagePanel
from .models import (
    NodeLabel,
    NodeProperty,
    NodeType,
    RelationshipProperty,
    RelationshipType,
)


def get_example_data(request):
    # Modify this function based on the actual data you want to retrieve
    node_labels = NodeLabel.objects.all()
    node_types = NodeType.objects.all()
    relationship_types = RelationshipType.objects.all()

    return {
        "node_labels": node_labels,
        "node_types": node_types,
        "relationship_types": relationship_types,
    }


layout = (
    HomePagePanel(
        name="Graph Schema",
        items=(
            HomePageItem(
                name="Node Labels",
                model=NodeLabel,
                weight=150,
                link="plugins:nautobot_graph:node_label_list",
                description="List node labels.",
                permissions=["nautobot_graph.view_nodelabel"],
            ),
            HomePageItem(
                name="Node Types",
                model=NodeType,
                weight=160,
                link="plugins:nautobot_graph:node_type_list",
                description="List node types.",
                permissions=["nautobot_graph.view_nodetype"],
            ),
            HomePageItem(
                name="Relationship Types",
                model=RelationshipType,
                weight=170,
                link="plugins:nautobot_graph:relationship_type_list",
                description="List relationship types.",
                permissions=["nautobot_graph.view_relationshiptype"],
            ),
        ),
    ),
    HomePagePanel(
        name="Graph Exploration",
        weight=250,
        items=(
            HomePageItem(
                name="Custom Graph Exploration",
                custom_template="item_graph_exploration.html",  # Adjust template name
                custom_data={"example_data": get_example_data},
                permissions=[
                    "nautobot_graph.view_nodelabel",
                    "nautobot_graph.view_nodetype",
                    "nautobot_graph.view_relationshiptype",
                ],
                weight=100,
            ),
        ),
    ),
    HomePagePanel(
        name="Custom Graph Exploration",
        custom_template="panel_graph_exploration.html",  # Adjust template name
        custom_data={"example_data": get_example_data},
        permissions=[
            "nautobot_graph.view_nodelabel",
            "nautobot_graph.view_nodetype",
            "nautobot_graph.view_relationshiptype",
        ],
        weight=350,
    ),
)
