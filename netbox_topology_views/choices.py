from django.utils.translation import gettext_lazy as _
from utilities.choices import ChoiceSet

class NodeLabelItems(ChoiceSet):
    DEVICE_NAME = 'devicename'
    DEVICE_TYPE = 'devicetype'
    ROLE = 'role'
    DESCRIPTION = 'description'
    PRIMARY_IPV4 = 'primaryipv4'
    PRIMARY_IPV6 = 'primaryipv6'
    OUT_OF_BAND_IP = 'outofbandip'
    PLATFORM = 'platform'
    SERIAL = 'serial'
    TENANT = 'tenant'
    SITE = 'site'
    LOCATION = 'location'
    RACK = 'rack'
    VIRTUAL_CHASSIS = 'virtualchassis'
    ASSET_TAG = 'assettag'

    CHOICES = [
        (DEVICE_NAME, _('Device Name')),
        (DEVICE_TYPE, _('Device Type')),
        (ROLE, _('Role')),
        (DESCRIPTION, _('Description')),
        (PRIMARY_IPV4, _('Primary IPv4')),
        (PRIMARY_IPV6, _('Primary IPv6')),
        (OUT_OF_BAND_IP, _('Out-of-band IP')),
        (PLATFORM, _('Platform')),
        (SERIAL, _('Serial')),
        (TENANT, _('Tenant')),
        (SITE, _('Site')),
        (LOCATION, _('Location')),
        (RACK, _('Rack')),
        (VIRTUAL_CHASSIS, _('Virtual Chassis')),
        (ASSET_TAG, _('Asset Tag')),
    ]
