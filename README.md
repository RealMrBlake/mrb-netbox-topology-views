# MRB NetBox Topology Views

Ein angepasster Fork von **NetBox Topology Views** mit erweiterten Rack-Ansichten,
interaktiver Kabelverfolgung und zusätzlichen Netzwerk-Icons.

Das Plugin erzeugt Topologien aus den in NetBox gepflegten Geräten, Ports und
Kabeln. Neben der klassischen Topologie bietet dieser Fork eine vollständige
Darstellung einzelner oder mehrerer Racks einschließlich Vorderseite,
Rückseite und Verkabelung.

## Vorteile dieses Forks

- Ein oder mehrere Racks gemeinsam anzeigen
- Geräte positionsgenau anhand ihrer Höheneinheiten darstellen
- Vorder- und Rückseite eines Racks getrennt betrachten
- Auf- und absteigende HE-Nummerierung sowie individuelle Start-HE automatisch berücksichtigen
- Rackübergreifende und externe Kabelverbindungen erkennen
- Geräte in der Kabeltopologie frei verschieben
- Geräte in der Kabeltopologie innerhalb jedes Racks nach ihrer Rackposition sortieren
- Kabeltopologie in den Browser-Vollbildmodus schalten
- Kabeltopologie zwischen 50 und 200 Prozent zoomen und im Vollbild scrollen
- Geräte in der Kabeltopologie mit rund 5 mm Abstand darstellen
- P2P-WirelessLinks und Multi-Access-WLANs als violette, gestrichelte Funkstrecken darstellen
- Funk-/WLAN-Verbindungen und Stromkabel in der Kabeltopologie der Rack-Ansicht optional ein-/ausblenden, farblich abgesetzt von Netzwerkkabeln (violett gestrichelt bzw. orange gepunktet)
- Manuelle Positionen pro Rack-Auswahl im Browser speichern
- Verbindungen eines Geräts beim Hover weiß hervorheben
- Alle verbundenen Ports und Gegenstellen eines Geräts anzeigen
- Schnittstellen eines Kabels beim Hover anzeigen
- Geräte und Kabel direkt aus der Topologie in NetBox öffnen
- Einzelne Racks, alle Racks oder die Kabeltopologie als SVG, PNG und draw.io exportieren
- Exporte grundsätzlich mit transparentem Hintergrund erzeugen
- Farben von Rackansicht und Export an den aktiven Light- oder Dark-Mode anpassen
- Topologie als PNG oder diagrams.net/draw.io-XML exportieren
- Zusätzliche Icons für Network-, Leaf-, Spine- und Aggregation-Switche
- Unterstützung für helle und dunkle NetBox-Themes

## Änderungen gegenüber dem Original

Dieser Fork ergänzt insbesondere:

1. Die neue Menükategorie **Weitere Ansichten**.
2. Eine Rack-Ansicht mit Filtern für Site, Location und mehrere Racks.
3. Positionsgenaue Rack-Elevations für Vorder- und Rückseite.
4. Eine Kabeltabelle mit A- und B-Terminierungen.
5. Eine interaktive, verschiebbare Kabeltopologie unter den Racks.
6. Hover-Hervorhebung und Port-zu-Port-Verfolgung für Geräte und Kabel.
7. Lokal gespeicherte Gerätepositionen und eine Funktion zum Zurücksetzen.
8. Ein erweitertes, skalierbares SVG-Iconset für Switch-Rollen.
9. Transparente SVG-, PNG- und draw.io-Exporte für Rack- und Topologieansichten.
10. Anpassungen für die Verwendung mit NetBox 4.6, darunter die geänderte
   `Rack.units`-Property.

## Vorschau

Die klassische Topologieansicht stammt aus dem ursprünglichen Plugin:

![Topology in light mode](doc/img/topology_light.png)
![Topology in dark mode](doc/img/topology_dark.png)

## Installation aus Gitea

Das Plugin kann direkt aus dem `develop`-Branch installiert werden:

```bash
/opt/netbox/venv/bin/pip install --upgrade --force-reinstall \
  "git+https://git.mrblake.cc/MrBlake/mrb-netbox-topology-views.git@develop"
```

Für eine reproduzierbare Produktivinstallation sollte statt `develop` ein
Release-Tag oder ein bestimmter Commit verwendet werden:

```bash
/opt/netbox/venv/bin/pip install --upgrade --force-reinstall \
  "git+https://git.mrblake.cc/MrBlake/mrb-netbox-topology-views.git@v4.5.1-mrb.1"
```

Für automatische Neuinstallationen bei einem NetBox-Upgrade wird derselbe
Eintrag in `/opt/netbox/local_requirements.txt` hinterlegt:

```text
git+https://git.mrblake.cc/MrBlake/mrb-netbox-topology-views.git@develop
```

Bei einem privaten Gitea-Repository muss der NetBox-Server Zugriff über einen
Deploy-Token oder SSH-Key erhalten.

## NetBox-Konfiguration

In `netbox/configuration.py` wird das Python-Paket aktiviert:

```python
PLUGINS = [
    "netbox_topology_views",
]

PLUGINS_CONFIG = {
    "netbox_topology_views": {
        "static_image_directory": "netbox_topology_views/img",
        "allow_coordinates_saving": True,
        "always_save_coordinates": False,
    },
}
```

Danach werden Migrationen und statische Dateien verarbeitet:

```bash
cd /opt/netbox/netbox
/opt/netbox/venv/bin/python manage.py migrate
/opt/netbox/venv/bin/python manage.py collectstatic --no-input
sudo systemctl restart netbox netbox-rq
```

Nach Änderungen an CSS oder Icons kann ein Hard-Reload des Browsers mit
`Strg+F5` erforderlich sein.

## Aktualisierung

```bash
/opt/netbox/venv/bin/pip install --upgrade --force-reinstall \
  "git+https://git.mrblake.cc/MrBlake/mrb-netbox-topology-views.git@develop"

cd /opt/netbox/netbox
/opt/netbox/venv/bin/python manage.py migrate
/opt/netbox/venv/bin/python manage.py collectstatic --no-input
sudo systemctl restart netbox netbox-rq
```

`--force-reinstall` ist derzeit sinnvoll, da der Fork intern noch die
Paketversion `4.5.1` verwendet.

## Verwendung

### Klassische Topologie

Unter **Plugins → Topology Views → Topology** steht die ursprüngliche,
filterbare Topologieansicht zur Verfügung. Sie unterstützt unter anderem:

- physische Kabel
- logische Verbindungen
- Nachbargeräte
- Circuit-Terminations
- Power Feeds
- Wireless Links
- Coordinate Groups
- PNG- und XML-Export

### Rack-Ansicht

Die erweiterte Ansicht befindet sich unter:

**Plugins → Topology Views → Weitere Ansichten → Rack-Ansicht**

Über Site, Location und Rack können ein einzelnes Rack oder mehrere Racks
ausgewählt werden. Optional lassen sich auch leere Racks einblenden.

In der Elevation werden Geräte entsprechend ihrer Position, Gerätehöhe und
Rack-Seite dargestellt. Unter den Elevations folgen:

1. die interaktive Kabeltopologie und
2. eine tabellarische Übersicht sämtlicher betroffener Kabel.

In der Kabeltopologie können Geräte per Drag-and-drop verschoben werden. Beim
Hover über ein Gerät werden dessen Kabel hervorgehoben und alle verbundenen
Ports aufgelistet. Beim Hover über ein Kabel erscheinen beide Terminierungen.
Ein Klick öffnet das jeweilige NetBox-Objekt.

Über die Export-Schaltflächen können ein einzelnes Rack, alle aktuell
angezeigten Racks oder die interaktive Kabeltopologie als SVG, PNG oder
draw.io-Datei gespeichert werden. Sämtliche Exportformate werden ohne
Hintergrundfläche erzeugt. Im draw.io-Export bleiben Rack-Rahmen, Geräte und
Beschriftungen als einzelne Elemente bearbeitbar. Topologiekabel werden als
echte Kanten exportiert und folgen den Geräten beim Verschieben in draw.io.

Die Positionen werden im `localStorage` des Browsers gespeichert. Sie gelten
damit nur für den jeweiligen Browser und die konkrete Rack-/Filterauswahl.

## Geräte-Icons

Das Plugin ordnet Icons anhand des Slugs einer Device Role zu. Dieser Fork
liefert zusätzlich folgende SVG-Dateien aus:

| Device-Role-Slug | Icon-Datei |
| --- | --- |
| `network-switch` | `network-switch.svg` |
| `leaf-switch` | `leaf-switch.svg` |
| `spine-switch` | `spine-switch.svg` |
| `aggregation-switch` | `aggregation-switch.svg` |

Eigene Bilder können weiterhin über die Seite **Images** zugeordnet werden.
Der Standardpfad lautet `netbox_topology_views/img` innerhalb von
`STATIC_ROOT`.

## Berechtigungen

Für die klassische Topologie werden mindestens folgende Rechte benötigt:

- `dcim.view_site`
- `dcim.view_device`

Für die Rack-Ansicht werden benötigt:

- `dcim.view_rack`
- `dcim.view_device`
- `dcim.view_cable`

Für das Speichern klassischer Topologiekoordinaten werden zusätzlich die
entsprechenden Rechte auf `netbox_topology_views.coordinate` benötigt.

## Kompatibilität

Die Basis dieses Forks ist NetBox Topology Views `4.5.1`. Die neuen
Rack-Funktionen wurden für den Einsatz mit NetBox `4.6.5` angepasst und das
Plugin ist für NetBox `4.7.x` (`min_version`/`max_version` in
`netbox_topology_views/__init__.py`) freigegeben. Da das ursprüngliche
Release offiziell für NetBox 4.5.x ausgewiesen ist, sollten Updates auf
neuere NetBox-Versionen zunächst in einer Testumgebung geprüft werden.

## Ursprung und Danksagung

Dieses Projekt ist ein Fork des Open-Source-Plugins
[NetBox Topology Views](https://github.com/mattieserver/netbox-topology-views).

Das ursprüngliche Plugin wurde von **Mattijs Vanhaverbeke** erstellt. Der
größte Teil der klassischen Topologieansicht, Datenmodelle, Filter und
Exportfunktionen basiert auf seiner Arbeit und den Beiträgen des ursprünglichen
Projekts.

Dieser Fork wird unabhängig weiterentwickelt und ist nicht mit dem
ursprünglichen Autor oder dem NetBox-Projekt offiziell verbunden.

## Lizenz

Das Projekt steht wie das Original unter der
[Apache License 2.0](LICENSE). Bestehende Copyright-, Lizenz- und
Urheberhinweise des ursprünglichen Projekts bleiben erhalten.
