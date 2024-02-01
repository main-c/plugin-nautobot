from typing import Any
from nautobot_graph.models import (
    NodeLabel,
    NodeProperty,
    NodeType,
    RelationshipProperty,
    RelationshipType,
)
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Test data for nautobot-graph."""

    def handle(self, *args: Any, **options: Any) -> str | None:
        self.stdout.write("Loading test data for nautobot-graph")
        # creating node labels
        for label in ["Device", "Site", "Cable"]:
            try:
                NodeLabel.objects.create(name=label)
            except Exception as e:
                continue

        # creating node types

        for node_type in [
            "Router",
            "Switch",
            "Firewall",
            "Server",
            "Access Switch",
            "Distribution Switch",
            "Core Switch",
        ]:
            try:
                NodeType.objects.create(
                    name=node_type, description=f"{node_type} node type"
                )
            except Exception as e:
                continue

        # creating node properties
        for node_type in NodeType.objects.all():
            for node_property in [
                "hostname",
                "serial_number",
                "vendor",
                "model",
                "site",
                "device_role",
                "device_type",
            ]:
                try:
                    NodeProperty.objects.create(
                        name=node_property, node_type=node_type, data_type="string"
                    )
                except Exception as e:
                    continue

        # creating relationship types
        for relationship_type in ["Connects", "Depends on", "Contains"]:
            try:
                RelationshipType.objects.create(
                    name=relationship_type,
                    description=f"{relationship_type} relationship",
                )
            except Exception as e:
                continue

        # creating relationship properties
        for relationship_type in RelationshipType.objects.all():
            for relationship_property in ["description", "cable"]:
                try:
                    RelationshipProperty.objects.create(
                        name=relationship_property,
                        relationship_type=relationship_type,
                        data_type="string",
                    )
                except Exception as e:
                    continue

        self.stdout.write("Test data loaded")
