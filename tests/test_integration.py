import pathlib
import yaml

import nomenclature


def test_integration_common_definitions():

    config_file = "nomenclature.yaml"
    config = {
        "repositories": {
            "common-definitions": {
                "url": "https://github.com/IAMconsortium/common-definitions.git/"
            }
        },
        "definitions": {
            "region": {"repository": "common-definitions"},
            "variable": {"repository": "common-definitions"},
        },
    }

    with open(config_file, "w") as file:
        yaml.dump(config, file)

    nomenclature.DataStructureDefinition("definitions")

    pathlib.Path(config_file).unlink()
