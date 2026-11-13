# Modified by MrBlake for the MRB NetBox Topology Views fork: https://git.mrblake.cc/MrBlake/mrb-netbox-topology-views
# Based on mattieserver/netbox-topology-views (Apache License 2.0). See the LICENSE and NOTICE files.
from netbox.plugins import PluginConfig


class TopologyViewsConfig(PluginConfig):
    name = "netbox_topology_views"
    verbose_name = "Topology views"
    description = "A plugin to render topology maps"
    version = "4.5.2"
    author = "Mattijs Vanhaverbeke (original), MrBlake (fork)"
    base_url = "netbox_topology_views"
    min_version = "4.7.0"
    max_version = "4.7.99"
    required_settings = []
    default_settings = {
        "static_image_directory": "netbox_topology_views/img",
        "allow_coordinates_saving": False,
        "always_save_coordinates": False,
    }

    def ready(self):
        from . import signals

        super().ready()


config = TopologyViewsConfig
