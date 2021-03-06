import os
import re


# A directory does not have a extension hence no '.'
def is_directory(file_name): return file_name.find('.') == -1


# This file pattern is expected from a test file
file_pattern = re.compile("test[a-zA-Z0-9_]*.py")
# Is test file
def is_test_file(file_name): return file_pattern.match(file_name)


# If the test file name is sample_test.py, module name is sample_test therefore get rid of .py part
def map_to_module_name(file_name): return file_name.split('.')[0]


def load_unit_test_modules(unit_test_directory, module_prefix=''):
    test_modules = []
    # Load files in the directory
    files_in_directory = os.listdir(unit_test_directory)

    # If no files, return empty list
    if not files_in_directory:
        return []

    nested_directories = filter(is_directory, files_in_directory)

    for nested_directory in nested_directories:
        # nested modules are accessed using '.', there add the prefix
        nested_test_modules = load_unit_test_modules(unit_test_directory.joinpath(nested_directory),
                                                     nested_directory + '.')
        for nested_test_module in nested_test_modules:
            test_modules.append(module_prefix + nested_test_module)

    test_files = filter(is_test_file, files_in_directory)
    test_module_names = list(map(map_to_module_name, test_files))
    # Append each test module
    for test_module in test_module_names:
        # Append the module prefix to test module name
        test_modules.append(module_prefix + test_module)

    return test_modules

