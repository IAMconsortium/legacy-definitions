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

    try:
        dsd = nomenclature.DataStructureDefinition("definitions")

        existing_variables = list(dsd.variable)
        legacy_variables = {}
        for code, attrs in dsd.variable.items():
            for project in ["navigate", "engage", "shape"]:
                if project in attrs.extra_attributes:
                    legacy_var = attrs.__getattr__(project)
                    if legacy_var != code and legacy_var in existing_variables:
                        legacy_variables[legacy_var] = code

        if legacy_variables:
            error = [
                f"'{legacy_var}' -> '{code}'" + "\n"
                for legacy_var, code in legacy_variables.items()
            ]

            raise ValueError(
                "Deprecated variables from legacy projects:\n" f"{''.join(error)}"
            )

    finally:
        pathlib.Path(config_file).unlink()
