from nautobot.apps.filters import BaseFilterSet, SearchFilter
from nautobot_graph.models import (
    NodeLabel,
    NodeProperty,
    NodeType,
    RelationshipProperty,
    RelationshipType,
)


class NodeLabelFilterSet(BaseFilterSet):
    """API filter for filtering nodelabel model objects."""

    q = SearchFilter(
        filter_predicates={
            "name": "icontains",
        },
    )

    class Meta:
        model = NodeLabel
        fields = [
            "name",
        ]


class NodePropertyFilterSet(BaseFilterSet):
    """API filter for filtering nodeproperty model objects."""

    q = SearchFilter(
        filter_predicates={
            "name": "icontains",
        },
    )

    class Meta:
        model = NodeProperty
        fields = [
            "name",
            "node_type",
        ]


class NodeTypeFilterSet(BaseFilterSet):
    """API filter for filtering nodetype model objects."""

    q = SearchFilter(
        filter_predicates={
            "name": "icontains",
            "description": "icontains",
        },
    )

    class Meta:
        model = NodeType
        fields = ["name", "description"]


class RelationshipTypeFilterSet(BaseFilterSet):
    """API filter for filtering relationshiptype model objects."""

    q = SearchFilter(
        filter_predicates={
            "name": "icontains",
            "description": "icontains",
            "src_node_type": "icontains",
            "dst_node_type": "icontains",
        },
    )

    class Meta:
        model = RelationshipType
        fields = ["name", "description", "src_node_type", "dst_node_type"]


class RelationshipPropertyFilterSet(BaseFilterSet):
    """API filter for filtering relationshipproperty model objects."""

    q = SearchFilter(
        filter_predicates={
            "name": "icontains",
            "relationship_type": "icontains",
        },
    )

    class Meta:
        model = RelationshipProperty
        fields = ["name", "relationship_type", "data_type"]
