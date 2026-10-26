from django.utils.translation import gettext_lazy as _
from netbox.plugins import PluginConfig


class TopologyViewsConfig(PluginConfig):
    name = "netbox_topology_views"
    verbose_name = _("Topology views")
    description = _("A plugin to render topology maps")
    version = "4.5.2"
    author = "Mattijs Vanhaverbeke, Codex & Claude"
    author_email = "author@example.com"
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
