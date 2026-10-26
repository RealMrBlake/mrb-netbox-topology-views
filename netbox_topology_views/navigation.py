from django.utils.translation import gettext_lazy as _
from netbox.plugins import PluginMenu, PluginMenuItem, PluginMenuButton

coordinategroup_buttons = (
    PluginMenuButton(
        link='plugins:netbox_topology_views:coordinategroup_add',
        title=_('Add'),
        icon_class='mdi mdi-plus-thick',
        permissions=['netbox_topology_views.add_coordinategroup']
    ),
    PluginMenuButton(
        link='plugins:netbox_topology_views:coordinategroup_import',
        title=_('Import'),
        icon_class='mdi mdi-upload',
        permissions=['netbox_topology_views.add_coordinategroup']
    )
)

circuitcoordinate_buttons = (
    PluginMenuButton(
        link='plugins:netbox_topology_views:circuitcoordinate_add',
        title=_('Add'),
        icon_class='mdi mdi-plus-thick',
        permissions=['netbox_topology_views.add_coordinate']
    ),
    PluginMenuButton(
        link='plugins:netbox_topology_views:circuitcoordinate_import',
        title=_('Import'),
        icon_class='mdi mdi-upload',
        permissions=['netbox_topology_views.add_coordinate']
    )
)

powerpanelcoordinate_buttons = (
    PluginMenuButton(
        link='plugins:netbox_topology_views:powerpanelcoordinate_add',
        title=_('Add'),
        icon_class='mdi mdi-plus-thick',
        permissions=['netbox_topology_views.add_coordinate']
    ),
    PluginMenuButton(
        link='plugins:netbox_topology_views:powerpanelcoordinate_import',
        title=_('Import'),
        icon_class='mdi mdi-upload',
        permissions=['netbox_topology_views.add_coordinate']
    )
)

powerfeedcoordinate_buttons = (
    PluginMenuButton(
        link='plugins:netbox_topology_views:powerfeedcoordinate_add',
        title=_('Add'),
        icon_class='mdi mdi-plus-thick',
        permissions=['netbox_topology_views.add_coordinate']
    ),
    PluginMenuButton(
        link='plugins:netbox_topology_views:powerfeedcoordinate_import',
        title=_('Import'),
        icon_class='mdi mdi-upload',
        permissions=['netbox_topology_views.add_coordinate']
    )
)

coordinate_buttons = (
    PluginMenuButton(
        link='plugins:netbox_topology_views:coordinate_add',
        title=_('Add'),
        icon_class='mdi mdi-plus-thick',
        permissions=['netbox_topology_views.add_coordinate']
    ),
    PluginMenuButton(
        link='plugins:netbox_topology_views:coordinate_import',
        title=_('Import'),
        icon_class='mdi mdi-upload',
        permissions=['netbox_topology_views.add_coordinate']
    )
)

menu = PluginMenu(
    label=_('Topology Views'),
    icon_class="mdi mdi-sitemap",
    groups=(
        (_('Topology'),
            (
                PluginMenuItem(link="plugins:netbox_topology_views:home", link_text=_("Topology"), permissions=["dcim.view_site", "dcim.view_device"]),
            ),
        ),
        (_('More views'),
            (
                PluginMenuItem(link="plugins:netbox_topology_views:rack_elevation", link_text=_("Rack view"), permissions=["dcim.view_rack", "dcim.view_device", "dcim.view_cable"]),
            ),
        ),
        (_('Coordinates'),
            (
                PluginMenuItem(link="plugins:netbox_topology_views:coordinategroup_list", link_text=_("Coordinate Groups"), buttons=coordinategroup_buttons, permissions=['netbox_topology_views.view_coordinategroup']),
                PluginMenuItem(link="plugins:netbox_topology_views:coordinate_list", link_text=_("Device Coordinates"), buttons=coordinate_buttons, permissions=['netbox_topology_views.view_coordinate']),
                PluginMenuItem(link="plugins:netbox_topology_views:powerfeedcoordinate_list", link_text=_("Power Feed Coords"), buttons=powerfeedcoordinate_buttons, permissions=['netbox_topology_views.view_coordinate']),
                PluginMenuItem(link="plugins:netbox_topology_views:powerpanelcoordinate_list", link_text=_("Power Panel Coords"), buttons=powerpanelcoordinate_buttons, permissions=['netbox_topology_views.view_coordinate']),
                PluginMenuItem(link="plugins:netbox_topology_views:circuitcoordinate_list", link_text=_("Circuit Coordinates"), buttons=circuitcoordinate_buttons, permissions=['netbox_topology_views.view_coordinate']),
            ),
        ),
        (_('Preferences'),
            (
                PluginMenuItem(link="plugins:netbox_topology_views:images", link_text=_("Images"), permissions=[ "dcim.view_site","dcim.view_devicerole"]),
                PluginMenuItem(link="plugins:netbox_topology_views:individualoptions", link_text=_("Individual Options"), permissions=['netbox_topology_views.change_individualoptions']),
            ),
        ),
    ),
)
