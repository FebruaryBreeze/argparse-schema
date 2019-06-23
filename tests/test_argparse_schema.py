import unittest
from pathlib import Path

import argparse_schema


class MyTestCase(unittest.TestCase):
    def test_argparse_schema(self):
        schema_path = Path(__file__).parent / 'argument_config.json'

        result = argparse_schema.parse(schema_path, [
            '/path/to/config',
            '--resume',
            '--scale', '2.0'
        ])
        self.assertEqual(result, {
            'config': '/path/to/config',
            'resume': True,
            'scale': 2.0,
            'mode': 'happy'
        })

        result = argparse_schema.parse(schema_path, [
            '/path/to/config',
            '--mode',
            'high'
        ])
        self.assertEqual(result, {
            'config': '/path/to/config',
            'resume': False,
            'scale': 1.0,
            'mode': 'high'
        })


if __name__ == '__main__':
    unittest.main()
