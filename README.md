# Nautobot Graph Plugin

A Django plugin for Nautobot that allows users to modify the schema of a graphical database through a web interface.The plugin supports managing node types, node properties, node labels, relationship types, and relationship properties. Data is stored in a PostgreSQL relational database. The plugin provides essential web operations, including creation, modification, deletion, and display of node and relationship types.

## Installation

To install this nautobot graph plugin from this directory run this command:

```no-highlight
pip install .
```

And then add it to your `PLUGINS` setting in your `nautobot_config.py`:

```python
PLUGINS = [
    "nautobot_graph",
]
```

Generate test data

```
nautobot-server test_data
```

