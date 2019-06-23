# argparse-schema [![Build Status](https://travis-ci.com/FebruaryBreeze/argparse-schema.svg?branch=master)](https://travis-ci.com/FebruaryBreeze/argparse-schema) [![codecov](https://codecov.io/gh/FebruaryBreeze/argparse-schema/branch/master/graph/badge.svg)](https://codecov.io/gh/FebruaryBreeze/argparse-schema) [![PyPI version](https://badge.fury.io/py/argparse-schema.svg)](https://pypi.org/project/argparse-schema/)

Parse Argument with JSON Schema.

## Installation

Need Python 3.6+.

```bash
pip install argparse-schema
```

## Usage

[Schema](./tests/argument_config.json):

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "title": "argument_config",
  "description": "Arg-parse Schema UnitTest",
  "type": "object",
  "properties": {
    "config": {
      "type": "string",
      "positional": true,
      "description": "path of config file"
    },
    "resume": {
      "type": "boolean",
      "description": "resume from checkpoint or not"
    },
    "scale": {
      "type": "number",
      "default": 1.0,
      "description": "scale of image"
    },
    "mode": {
      "enum": [
        "happy",
        "high",
        "heaven"
      ],
      "default": "happy",
      "description": "speed mode"
    }
  },
  "required": [
    "config"
  ]
}
```

Python Code:

```python
# demo.py
import argparse_schema

print(argparse_schema.parse(schema='./tests/argument_config.json'))
```

Run with arguments:

```bash
python3 demo.py /path/to/config.py
#> {'config': '/path/to/config.py', 'resume': False, 'scale': 1.0, 'mode': 'happy'}
```

CLI:

```bash
argparse-schema tests/argument_config.json
#> Show help for schema file [tests/argument_config.json]:
#> usage: YOUR-COMMAND [-h] [--resume] [--scale SCALE]
#>                     [--mode {happy,high,heaven}]
#>                     config
#>
#> Arg-parse Schema UnitTest
#>
#> positional arguments:
#>   config                path of config file
#>
#> optional arguments:
#>   -h, --help            show this help message and exit
#>   --resume              resume from checkpoint or not
#>   --scale SCALE         scale of image, [1.0] in default
#>   --mode {happy,high,heaven}
#>                         speed mode, [happy] in default
```
