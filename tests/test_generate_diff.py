import os
import pytest
from gendiff import generate_diff


current_dir = os.path.dirname(os.path.abspath(__file__))


stylish_plain_result = os.path.join(current_dir, 'fixtures/stylish_plain_result')
stylish_nested_result = os.path.join(current_dir, 'fixtures/stylish_nested_result')
plain_nested_result = os.path.join(current_dir, 'fixtures/plain_nested_result')
json_nested_result = os.path.join(current_dir, 'fixtures/json_nested_result')


def read_result(file_path):
    with open(file_path) as file:
        return file.read()


file1_plain_json = os.path.join(current_dir, 'fixtures/file1_plain.json')
file2_plain_json = os.path.join(current_dir, 'fixtures/file2_plain.json')


file1_plain_yaml = os.path.join(current_dir, 'fixtures/file1_plain.yaml')
file2_plain_yaml = os.path.join(current_dir, 'fixtures/file2_plain.yaml')


file1_plain_yml = os.path.join(current_dir, 'fixtures/file1_plain.yml')
file2_plain_yml = os.path.join(current_dir, 'fixtures/file2_plain.yml')


file1_json = os.path.join(current_dir, 'fixtures/file1.json')
file2_json = os.path.join(current_dir, 'fixtures/file2.json')


file1_yaml = os.path.join(current_dir, 'fixtures/file1.yaml')
file2_yaml = os.path.join(current_dir, 'fixtures/file2.yaml')


file1_yml = os.path.join(current_dir, 'fixtures/file1.yml')
file2_yml = os.path.join(current_dir, 'fixtures/file2.yml')


test_cases = [
    (file1_plain_json, file2_plain_json, 'stylish', stylish_plain_result),
    (file1_plain_yaml, file2_plain_yaml, 'stylish', stylish_plain_result),
    (file1_plain_yml, file2_plain_yml, 'stylish', stylish_plain_result),
    (file1_json, file2_json, 'stylish', stylish_nested_result),
    (file1_yaml, file2_yaml, 'stylish', stylish_nested_result),
    (file1_yml, file2_yml, 'stylish', stylish_nested_result),
    (file1_json, file2_json, 'plain', plain_nested_result),
    (file1_yaml, file2_yaml, 'plain', plain_nested_result),
    (file1_yml, file2_yml, 'plain', plain_nested_result),
    (file1_json, file2_json, 'json', json_nested_result),
    (file1_yaml, file2_yaml, 'json', json_nested_result),
    (file1_yml, file2_yml, 'json', json_nested_result)
]


@pytest.mark.parametrize('file1, file2, formatter, result_file', test_cases)
def test_generate_diff(file1, file2, formatter, result_file):
    assert generate_diff(file1, file2, formatter) == read_result(result_file)
