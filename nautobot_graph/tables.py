import django_tables2 as tables

from nautobot.apps.tables import (
    BaseTable,
    ButtonsColumn,
    ToggleColumn,
)

from nautobot_graph.models import (
    NodeLabel,
    NodeProperty,
    NodeType,
    RelationshipProperty,
    RelationshipType,
)


class NodeLabelTable(BaseTable):
    """Table for list view of `NodeLabel` objects."""

    pk = ToggleColumn()
    name = tables.LinkColumn()
    actions = ButtonsColumn(NodeLabel)

    class Meta(BaseTable.Meta):
        model = NodeLabel
        fields = [
            "pk",
            "name",
        ]


class NodePropertyTable(BaseTable):
    """Table for list view of `NodeProperty` objects."""

    pk = ToggleColumn()
    name = tables.LinkColumn()
    actions = ButtonsColumn(NodeProperty)

    class Meta(BaseTable.Meta):
        model = NodeProperty
        fields = ["pk", "name", "node_type", "data_type"]


class NodeTypeTable(BaseTable):
    """Table for list view of `NodeType` objects."""

    pk = ToggleColumn()
    name = tables.LinkColumn()
    actions = ButtonsColumn(NodeType)

    class Meta(BaseTable.Meta):
        model = NodeType
        fields = [
            "pk",
            "name",
            "description",
        ]


class RelationshipPropertyTable(BaseTable):
    """Table for list view of `RelationshipProperty` objects."""

    pk = ToggleColumn()
    name = tables.LinkColumn()
    actions = ButtonsColumn(RelationshipProperty)

    class Meta(BaseTable.Meta):
        model = RelationshipProperty
        fields = ["pk", "name", "relationship_type", "data_type"]


class RelationshipTypeTable(BaseTable):
    """Table for list view of `RelationshipType` objects."""

    pk = ToggleColumn()
    name = tables.LinkColumn()
    actions = ButtonsColumn(RelationshipType)

    class Meta(BaseTable.Meta):
        model = RelationshipType
        fields = ["pk", "name", "src_node_type", "dst_node_type"]
