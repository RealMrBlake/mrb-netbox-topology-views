"""Keeps the NetBox range in README.md in sync with the PluginConfig."""
import ast
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def plugin_versions():
    tree = ast.parse((ROOT / "netbox_topology_views" / "__init__.py").read_text())
    values = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Constant):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id in ("min_version", "max_version"):
                    values[target.id] = node.value.value
    return values["min_version"], values["max_version"]


def expected_range(min_version, max_version):
    upper = re.sub(r"\.99$", ".x", max_version)
    if min_version.endswith(".0") and upper == min_version[:-2] + ".x":
        return f"`{upper}`"
    return f"`{min_version}` – `{upper}`"


class MetadataTest(unittest.TestCase):
    def test_readme_matches_plugin_config(self):
        readme = (ROOT / "README.md").read_text()
        expected = expected_range(*plugin_versions())
        self.assertIn(f"| **NetBox** | {expected} |", readme)
        self.assertIn(f"- NetBox {expected}", readme)


if __name__ == "__main__":
    unittest.main()
