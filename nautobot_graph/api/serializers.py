from rest_framework import serializers

from nautobot.apps.api import NautobotModelSerializer

from nautobot_graph.models import (
    NodeLabel,
    NodeProperty,
    NodeType,
    RelationshipProperty,
    RelationshipType,
)

# class AnotherExampleModelSerializer(NautobotModelSerializer):
#     """Used for normal CRUD operations."""

#     url = serializers.HyperlinkedIdentityField(
#         view_name="plugins-api:nautobot_graph-api:anotherexamplemodel-detail"
#     )

#     class Meta:
#         model = AnotherExampleModel
#         fields = "__all__"


class NodeLabelSerializer(NautobotModelSerializer):
    """Used for normal CRUD operations."""

    # url = serializers.HyperlinkedIdentityField(
    #     view_name="plugins-api:nautobot_graph-api:nodelabel-detail"
    # )

    class Meta:
        model = NodeLabel
        fields = ("name",)


class NodeTypeSerializer(NautobotModelSerializer):
    """Used for normal CRUD operations."""

    # url = serializers.HyperlinkedIdentityField(
    #     view_name="plugins-api:nautobot_graph-api:nodetype-detail"
    # )

    class Meta:
        model = NodeType
        fields = ("name", "description")


class NodePropertySerializer(NautobotModelSerializer):
    """Used for normal CRUD operations."""

    # url = serializers.HyperlinkedIdentityField(
    #     view_name="plugins-api:nautobot_graph-api:nodeproperty-detail"
    # )

    node_type = NodeTypeSerializer()

    class Meta:
        model = NodeProperty
        fields = ("name", "node_type", "data_type")


class RelationshipTypeSerializer(NautobotModelSerializer):
    """Used for normal CRUD operations."""

    # url = serializers.HyperlinkedIdentityField(
    #     view_name="plugins-api:nautobot_graph-api:relationshiptype-detail"
    # )

    class Meta:
        model = RelationshipType
        fields = ("name", "description")


class RelationshipPropertySerializer(NautobotModelSerializer):
    """Used for normal CRUD operations."""

    # url = serializers.HyperlinkedIdentityField(
    #     view_name="plugins-api:nautobot_graph-api:relationshipproperty-detail"
    # )
    relationship_type = RelationshipTypeSerializer()

    class Meta:
        model = RelationshipProperty
        fields = ("name", "relationship_type", "data_type")
