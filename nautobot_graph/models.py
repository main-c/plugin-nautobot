from django.db import models

from nautobot.apps.models import OrganizationalModel

# models.py
# Define primitive data types for node and relationship properties
DATATYPE_CHOICES = (
    ("string", "String"),
    ("integer", "Integer"),
    ("float", "Float"),
    ("boolean", "Boolean"),
    ("date", "Date"),
    ("datetime", "DateTime"),
)


class NodeType(OrganizationalModel):
    """A type of node in the graph"""

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class NodeProperty(OrganizationalModel):
    """A property of a node type"""

    name = models.CharField(max_length=255)
    node_type = models.ForeignKey(NodeType, on_delete=models.CASCADE)
    data_type = models.CharField(max_length=50, choices=DATATYPE_CHOICES)

    def __str__(self):
        return f"{self.node_type.name} - {self.name}"

    class Meta:
        # This should be unique per relationship type
        unique_together = ("name", "node_type")


class NodeLabel(OrganizationalModel):
    """A label for a node type"""

    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class RelationshipType(OrganizationalModel):
    """A type of relationship between nodes"""

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    src_node_type = models.ForeignKey(
        NodeType,
        on_delete=models.CASCADE,
        related_name="src_relationships",
        null=True,
        blank=True,
    )
    dst_node_type = models.ForeignKey(
        NodeType,
        on_delete=models.CASCADE,
        related_name="dst_relationships",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class RelationshipProperty(OrganizationalModel):
    """A property of a relationship type"""

    name = models.CharField(max_length=255)
    relationship_type = models.ForeignKey(RelationshipType, on_delete=models.CASCADE)
    data_type = models.CharField(max_length=50, choices=DATATYPE_CHOICES)

    def __str__(self):
        return f"{self.relationship_type.name} - {self.name}"

    class Meta:
        # This should be unique per relationship type
        unique_together = ("name", "relationship_type")
