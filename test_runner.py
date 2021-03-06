import unittest
import importlib
from pathlib import Path

from test_loader import load_unit_test_modules

# Define a loader to load files and suite to load suites
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# current_directory = Path(__file__)
current_file = Path(__file__)
current_directory = current_file.parent

unit_test_directory = current_directory.joinpath('tests')

test_modules = load_unit_test_modules(unit_test_directory, 'tests.')

for test_module in test_modules:
    module = importlib.import_module(test_module)
    suite.addTest(loader.loadTestsFromModule(module))


runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

