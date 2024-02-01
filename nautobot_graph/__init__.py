from importlib import metadata

__version__ = metadata.version(__name__)


from nautobot.apps import (
    nautobot_database_ready,
    NautobotAppConfig,
)

from nautobot_graph.signals import nautobot_database_ready_callback


class NautobotGraphPluginConfig(NautobotAppConfig):
    name = "nautobot_graph"
    verbose_name = "Nautobot Graph App"
    author = "Yannik KADJIE"
    author_email = "yannikkwc@example.com"
    version = __version__
    description = """A Django plugin for Nautobot that allows users to modify the schema of a graphical database through a web interface.
                    The plugin supports managing node types, node properties, node labels, relationship types, and relationship properties.
                    Data is stored in a PostgreSQL relational database. The plugin provides essential web operations, including creation, modification, deletion, and display of node and relationship types.
                """
    base_url = "nautobot-graph"
    min_version = "0.9"
    max_version = "9.0"
    searchable_models = [
        "nodelabel",
        "nodeproperty",
        "nodetype",
        "relationshiptype",
        "relationshipproperty",
    ]

    # URL reverse lookup names
    home_view_name = "plugins:nautobot_graph:home"

    def ready(self):
        """Callback when this app is loaded."""
        super().ready()
        # Connect the nautobot_database_ready_callback() function to the nautobot_database_ready signal.
        # This is by no means a requirement for all plugins, but is a useful way for a plugin to perform
        # database operations such as defining CustomFields, Relationships, etc. at the appropriate time.
        nautobot_database_ready.connect(nautobot_database_ready_callback, sender=self)


config = NautobotGraphPluginConfig
