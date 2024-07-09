# Legacy-definitions

[![License: CC0-1.0](https://img.shields.io/github/license/iamConsortium/legacy-definitions)](https://github.com/IAMconsortium/legacy-definitions/blob/main/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

This repository contains variable definitions from the NAVIGATE project.

It is intended to be used complementary to the common-definitions repository while the
common definition repository is being developed.

## Intended use

The use case envisioned for this repository is as follows:

* For a new model comparison project common-definitions and legacy-definitions should be
  used as a base for the variable template
* Any additional variables which are part of the project should either be added to
  common-definitions if they are sufficiently general or to the project internal
  workflow if they are too specialized.

The `nomenclature.yaml` file for this configuration would look like this:

```yaml
repositories:
  common-definitions:
    url: https://github.com/iamconsortium/common-definitions
  legacy-definitions:
    url: https://github.com/iamconsortium/common-definitions
definitions:
  variable:
    repository: [common-definitions, legacy-definitions]
```

## Validation workflow

As the common-definitions repository is expected to become more comprehensive there will
be overlap with the legacy definitions. This will create errors in use.

In order to catch these errors early enough, the validation workflow is run once per day
at midnight.
