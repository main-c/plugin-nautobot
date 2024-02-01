from django.shortcuts import render
from django.views.generic import View

from nautobot.apps import views
from nautobot_graph import filters, forms, tables
from nautobot_graph.api import serializers
from nautobot_graph.models import (
    NodeLabel,
    NodeProperty,
    NodeType,
    RelationshipProperty,
    RelationshipType,
)


class NautobotGraphHomeView(View):
    def get(self, request):
        return render(request, "nautobot_graph/home.html")


class NodeLabelModelUIViewSet(views.NautobotUIViewSet):
    """
    A viewset for viewing and editing NodeLabel instances.

    """

    bulk_update_form_class = forms.NodeLabelBulkEditForm
    filterset_class = filters.NodeLabelFilterSet
    filterset_form_class = forms.NodeLabelFilterForm
    form_class = forms.NodeLabelForm
    queryset = NodeLabel.objects.all()
    table_class = tables.NodeLabelTable
    serializer_class = serializers.NodeLabelSerializer


class NodePropertyModelUIViewSet(views.NautobotUIViewSet):
    """
    A viewset for viewing and editing NodeProperty instances.
    """

    bulk_update_form_class = forms.NodePropertyBulkEditForm
    filterset_class = filters.NodePropertyFilterSet
    filterset_form_class = forms.NodePropertyFilterForm
    form_class = forms.NodePropertyForm
    queryset = NodeProperty.objects.all()
    table_class = tables.NodePropertyTable
    serializer_class = serializers.NodePropertySerializer


class NodeTypeModelUIViewSet(views.NautobotUIViewSet):
    """A viewset for viewing and editing NodeType instances."""

    bulk_update_form_class = forms.NodeTypeBulkEditForm
    filterset_class = filters.NodeTypeFilterSet
    filterset_form_class = forms.NodeTypeFilterForm
    form_class = forms.NodeTypeForm
    queryset = NodeType.objects.all()
    table_class = tables.NodeTypeTable
    serializer_class = serializers.NodeTypeSerializer


class RelationshipPropertyModelUIViewSet(views.NautobotUIViewSet):
    """A viewset for viewing and editing RelationshipProperty instances."""

    bulk_update_form_class = forms.RelationshipPropertyBulkEditForm
    filterset_class = filters.RelationshipPropertyFilterSet
    filterset_form_class = forms.RelationshipPropertyFilterForm
    form_class = forms.RelationshipPropertyForm
    queryset = RelationshipProperty.objects.all()
    table_class = tables.RelationshipPropertyTable
    serializer_class = serializers.RelationshipPropertySerializer


class RelationshipTypeModelUIViewSet(views.NautobotUIViewSet):
    """A viewset for viewing and editing RelationshipType instances."""

    bulk_update_form_class = forms.RelationshipTypeBulkEditForm
    filterset_class = filters.RelationshipTypeFilterSet
    filterset_form_class = forms.RelationshipTypeFilterForm
    form_class = forms.RelationshipTypeForm
    queryset = RelationshipType.objects.all()
    table_class = tables.RelationshipTypeTable
    serializer_class = serializers.RelationshipTypeSerializer
