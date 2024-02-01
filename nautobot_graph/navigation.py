from nautobot.apps.ui import (
    NavMenuAddButton,
    NavMenuGroup,
    NavMenuItem,
    NavMenuTab,
)

menu_items = (
    NavMenuTab(
        name="Plugins",
        groups=(
            NavMenuGroup(
                name="Nautobot Graph App",
                weight=100,
                items=(
                    NavMenuItem(
                        link="plugins:nautobot_graph:nodelabel_list",
                        name="Node Labels",
                        permissions=["nautobot_graph.view_nodelabel"],
                        buttons=(
                            NavMenuAddButton(
                                link="plugins:nautobot_graph:nodelabel_add",
                                permissions=[
                                    "nautobot_graph.add_nodelabel",
                                ],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="plugins:nautobot_graph:nodeproperty_list",
                        name="Node Properties",
                        permissions=["nautobot_graph.view_nodeproperty"],
                        buttons=(
                            NavMenuAddButton(
                                link="plugins:nautobot_graph:nodeproperty_add",
                                permissions=[
                                    "nautobot_graph.add_nodeproperty",
                                ],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="plugins:nautobot_graph:nodetype_list",
                        name="Node Types",
                        permissions=["nautobot_graph.view_nodetype"],
                        buttons=(
                            NavMenuAddButton(
                                link="plugins:nautobot_graph:nodetype_add",
                                permissions=[
                                    "nautobot_graph.add_nodetype",
                                ],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="plugins:nautobot_graph:relationshipproperty_list",
                        name="Relationship Properties",
                        permissions=["nautobot_graph.view_relationshipproperty"],
                        buttons=(
                            NavMenuAddButton(
                                link="plugins:nautobot_graph:relationshipproperty_add",
                                permissions=[
                                    "nautobot_graph.add_relationshipproperty",
                                ],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="plugins:nautobot_graph:relationshiptype_list",
                        name="Relationship Types",
                        permissions=["nautobot_graph.view_relationshiptype"],
                        buttons=(
                            NavMenuAddButton(
                                link="plugins:nautobot_graph:relationshiptype_add",
                                permissions=[
                                    "nautobot_graph.add_relationshiptype",
                                ],
                            ),
                        ),
                    ),
                ),
            ),
        ),
    ),
    NavMenuTab(
        name="Nautobot Graph Menu",
        groups=(
            NavMenuGroup(
                name="Node Exploration",
                weight=100,
                items=(
                    NavMenuItem(
                        link="plugins:nautobot_graph:nodelabel_list",
                        name="Node Labels",
                        permissions=["nautobot_graph.view_nodelabel"],
                        buttons=(
                            NavMenuAddButton(
                                link="plugins:nautobot_graph:nodelabel_add",
                                permissions=[
                                    "nautobot_graph.add_nodelabel",
                                ],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="plugins:nautobot_graph:nodeproperty_list",
                        name="Node Properties",
                        permissions=["nautobot_graph.view_nodeproperty"],
                        buttons=(
                            NavMenuAddButton(
                                link="plugins:nautobot_graph:nodeproperty_add",
                                permissions=[
                                    "nautobot_graph.add_nodeproperty",
                                ],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="plugins:nautobot_graph:nodetype_list",
                        name="Node Types",
                        permissions=["nautobot_graph.view_nodetype"],
                        buttons=(
                            NavMenuAddButton(
                                link="plugins:nautobot_graph:nodetype_add",
                                permissions=[
                                    "nautobot_graph.add_nodetype",
                                ],
                            ),
                        ),
                    ),
                ),
            ),
            NavMenuGroup(
                name="Relationship Exploration",
                weight=100,
                items=(
                    NavMenuItem(
                        link="plugins:nautobot_graph:relationshipproperty_list",
                        name="Relationship Properties",
                        permissions=["nautobot_graph.view_relationshipproperty"],
                        buttons=(
                            NavMenuAddButton(
                                link="plugins:nautobot_graph:relationshipproperty_add",
                                permissions=[
                                    "nautobot_graph.add_relationshipproperty",
                                ],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="plugins:nautobot_graph:relationshiptype_list",
                        name="Relationship Types",
                        permissions=["nautobot_graph.view_relationshiptype"],
                        buttons=(
                            NavMenuAddButton(
                                link="plugins:nautobot_graph:relationshiptype_add",
                                permissions=[
                                    "nautobot_graph.add_relationshiptype",
                                ],
                            ),
                        ),
                    ),
                ),
            ),
        ),
    ),
)
