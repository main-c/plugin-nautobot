from django.contrib import admin

from nautobot.apps.admin import NautobotModelAdmin

from nautobot_graph.models import (
    NodeLabel,
    NodeProperty,
    NodeType,
    RelationshipProperty,
    RelationshipType,
)


@admin.register(NodeLabel)
class NodeLabelAdmin(NautobotModelAdmin):
    """Admin for `NodeLabel` objects."""

    list_display = (
        "pk",
        "name",
    )
    search_fields = ("pk", "name")
    readonly_fields = ("pk", "name")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "pk",
                    "name",
                )
            },
        ),
    )
    add_fieldsets = (
        None,
        {"fields": ("name",)},
    )
    ordering = ("pk", "name")


@admin.register(NodeProperty)
class NodePropertyAdmin(NautobotModelAdmin):
    """Admin for `NodeProperty` objects."""

    list_display = ("pk", "name", "node_type", "data_type")
    search_fields = ("pk", "name", "node_type", "data_type")
    readonly_fields = ("pk", "name", "node_type", "data_type")
    fieldsets = (
       ( None,
        {
            "fields": (
                "pk",
                "name",
                "node_type",
                "data_type",
            )
        },),
    )
    add_fieldsets = (
        None,
        {
            "fields": (
                "name",
                "node_type",
                "data_type",
            )
        },
    )
    ordering = ("pk", "name", "node_type", "data_type")


@admin.register(NodeType)
class NodeTypeAdmin(NautobotModelAdmin):
    """Admin for `NodeType` objects."""

    list_display = ("pk", "name")
    search_fields = ("pk", "name")
    readonly_fields = ("pk", "name")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "pk",
                    "name",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {"fields": ("name",)},
        ),
    )
    ordering = ("pk", "name")


@admin.register(RelationshipProperty)
class RelationshipPropertyAdmin(NautobotModelAdmin):
    """Admin for `RelationshipProperty` objects."""

    list_display = ("pk", "name", "relationship_type", "data_type")
    search_fields = ("pk", "name", "relationship_type", "data_type")
    readonly_fields = ("pk", "name", "relationship_type", "data_type")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "pk",
                    "name",
                    "relationship_type",
                    "data_type",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "relationship_type",
                    "data_type",
                )
            },
        ),
    )
    ordering = ("pk", "name", "relationship_type", "data_type")


@admin.register(RelationshipType)
class RelationshipTypeAdmin(NautobotModelAdmin):
    """Admin for `RelationshipType` objects."""

    list_display = ("pk", "name")
    search_fields = ("pk", "name")
    readonly_fields = ("pk", "name")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "pk",
                    "name",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {"fields": ("name",)},
        ),
    )
    ordering = ("pk", "name")
