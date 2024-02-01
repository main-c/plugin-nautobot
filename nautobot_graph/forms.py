from django import forms

from nautobot.apps.forms import BootstrapMixin, BulkEditForm, NautobotModelForm

from nautobot_graph.models import (
    NodeType,
    NodeProperty,
    NodeLabel,
    RelationshipType,
    RelationshipProperty,
    DATATYPE_CHOICES,
)


class NodeTypeForm(NautobotModelForm):
    """Generic create/update form for `NodeType` objects."""

    class Meta:
        model = NodeType
        fields = ["name", "description"]


class NodePropertyForm(NautobotModelForm):
    """Generic create/update form for `NodeProperty` objects."""

    class Meta:
        model = NodeProperty
        fields = ["name", "node_type", "data_type"]


class NodeLabelForm(NautobotModelForm):
    """Generic create/update form for `NodeLabel` objects."""

    class Meta:
        model = NodeLabel
        fields = ["name"]


class RelationshipTypeForm(NautobotModelForm):
    """Generic create/update form for `RelationshipType` objects."""

    class Meta:
        model = RelationshipType
        fields = ["name", "description", "src_node_type", "dst_node_type"]


class RelationshipPropertyForm(NautobotModelForm):
    """Generic create/update form for `RelationshipProperty` objects."""

    class Meta:
        model = RelationshipProperty
        fields = ["name", "relationship_type", "data_type"]


class NodeLabelFilterForm(BootstrapMixin, forms.Form):
    """Filtering/search form for `Nodelabel` objects."""

    model = NodeLabel
    q = forms.CharField(required=False, label="Search")
    name = forms.CharField(max_length=20, required=False)


class NodeLabelBulkEditForm(BootstrapMixin, BulkEditForm):
    """Bulk edit form for `NodeLabel` objects."""

    pk = forms.ModelMultipleChoiceField(
        queryset=NodeLabel.objects.all(), widget=forms.MultipleHiddenInput
    )
    name = forms.CharField(max_length=20, required=False)

    class Meta:
        nullable_fields = []


class NodePropertyFilterForm(BootstrapMixin, forms.Form):
    """Filtering/search form for `NodeProperty` objects."""

    model = NodeProperty
    q = forms.CharField(required=False, label="Search")
    name = forms.CharField(max_length=20, required=False)
    node_type = forms.ModelChoiceField(queryset=NodeType.objects.all(), required=False)
    data_type = forms.ChoiceField(required=False, choices=DATATYPE_CHOICES)


class NodePropertyBulkEditForm(BootstrapMixin, BulkEditForm):
    """Bulk edit form for `NodeProperty` objects."""

    pk = forms.ModelMultipleChoiceField(
        queryset=NodeProperty.objects.all(), widget=forms.MultipleHiddenInput
    )
    name = forms.CharField(max_length=20, required=False)
    node_type = forms.ModelChoiceField(queryset=NodeType.objects.all(), required=False)
    data_type = forms.ChoiceField(required=False, choices=DATATYPE_CHOICES)

    class Meta:
        nullable_fields = []


class NodeTypeFilterForm(BootstrapMixin, forms.Form):
    """Filtering/search form for `NodeType` objects."""

    model = NodeType
    q = forms.CharField(required=False, label="Search")
    name = forms.CharField(max_length=20, required=False)


class NodeTypeBulkEditForm(BootstrapMixin, BulkEditForm):
    """Bulk edit form for `NodeType` objects."""

    pk = forms.ModelMultipleChoiceField(
        queryset=NodeType.objects.all(), widget=forms.MultipleHiddenInput
    )
    name = forms.CharField(max_length=20, required=False)
    description = forms.CharField(max_length=200, required=False)

    class Meta:
        nullable_fields = []


class RelationshipTypeFilterForm(BootstrapMixin, forms.Form):
    """Filtering/search form for `RelationshipType` objects."""

    model = RelationshipType
    q = forms.CharField(required=False, label="Search")
    name = forms.CharField(max_length=20, required=False)


class RelationshipTypeBulkEditForm(BootstrapMixin, BulkEditForm):
    """Bulk edit form for `RelationshipType` objects."""

    pk = forms.ModelMultipleChoiceField(
        queryset=RelationshipType.objects.all(), widget=forms.MultipleHiddenInput
    )
    name = forms.CharField(max_length=20, required=False)
    description = forms.CharField(max_length=200, required=False)
    src_node_type = forms.ModelChoiceField(
        queryset=NodeType.objects.all(), required=False
    )
    dst_node_type = forms.ModelChoiceField(
        queryset=NodeType.objects.all(), required=False
    )

    class Meta:
        nullable_fields = []


class RelationshipPropertyFilterForm(BootstrapMixin, forms.Form):
    """Filtering/search form for `RelationshipProperty` objects."""

    model = RelationshipProperty
    q = forms.CharField(required=False, label="Search")
    name = forms.CharField(max_length=20, required=False)
    relationship_type = forms.ModelChoiceField(
        queryset=RelationshipType.objects.all(), required=False
    )
    data_type = forms.ChoiceField(required=False, choices=DATATYPE_CHOICES)


class RelationshipPropertyBulkEditForm(BootstrapMixin, BulkEditForm):
    """Bulk edit form for `RelationshipProperty` objects."""

    pk = forms.ModelMultipleChoiceField(
        queryset=RelationshipProperty.objects.all(), widget=forms.MultipleHiddenInput
    )
    name = forms.CharField(max_length=20, required=False)
    relationship_type = forms.ModelChoiceField(
        queryset=RelationshipType.objects.all(), required=False
    )
    data_type = forms.ChoiceField(required=False, choices=DATATYPE_CHOICES)

    class Meta:
        nullable_fields = []
