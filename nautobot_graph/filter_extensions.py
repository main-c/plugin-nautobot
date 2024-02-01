from django import forms

from nautobot.apps.filters import (
    FilterExtension,
    MultiValueCharFilter,
    NaturalKeyOrPKMultipleChoiceFilter,
)
from nautobot.apps.forms import DynamicModelMultipleChoiceField
from nautobot.tenancy.models import Tenant


def suffix_search(queryset, name, value):
    return queryset.filter(description=f"{value[0]}.nautobot.com")


class TenantFilterExtension(FilterExtension):
    """Test instance showing both filterset_fields and filterform_fields in action."""

    model = "tenancy.tenant"

    filterset_fields = {
        "nautobot_graph_description": MultiValueCharFilter(
            field_name="description", label="Description"
        ),
        "nautobot_graph_sdescrip": MultiValueCharFilter(
            field_name="description", label="Description", method=suffix_search
        ),
        "nautobot_graph_dtype": MultiValueCharFilter(
            field_name="locations__devices__device_type__model",
            label="Device Type (model)",
        ),
    }

    filterform_fields = {
        "nautobot_graph_description": forms.CharField(
            required=False, label="Description"
        ),
        "nautobot_graph_dtype": forms.CharField(required=False, label="Device Type"),
        "name__ic": forms.CharField(required=False, label="Name Contains"),
        "nautobot_graph_sdescrip": forms.CharField(
            required=False, label="Suffix Description"
        ),
    }


class DeviceFilterExtension(FilterExtension):
    """Created to test that filterset_fields and filterform_fields being empty dicts is fine."""

    model = "dcim.device"


class PrefixFilterExtension(FilterExtension):
    """Created to test filter extensions and Dynamic Group support."""

    model = "ipam.prefix"

    filterset_fields = {
        "nautobot_graph_prefix_tenant_name": NaturalKeyOrPKMultipleChoiceFilter(
            field_name="tenant",
            queryset=Tenant.objects.all(),
            to_field_name="name",
            label="Tenant Name",
        ),
    }

    filterform_fields = {
        "nautobot_graph_prefix_tenant_name": DynamicModelMultipleChoiceField(
            queryset=Tenant.objects.all(),
            to_field_name="name",
            required=False,
            label="Tenant Name",
        )
    }


filter_extensions = [
    TenantFilterExtension,
    DeviceFilterExtension,
    PrefixFilterExtension,
]