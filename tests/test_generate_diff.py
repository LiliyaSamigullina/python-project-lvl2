import os
from gendiff import generate_diff


current_dir = os.path.dirname(os.path.abspath(__file__))


with open(os.path.join(current_dir, 'fixtures/stylish_plain_result')) as file:
    stylish_plain_result = file.read()

with open(os.path.join(current_dir, 'fixtures/stylish_nested_result')) as file:
    stylish_nested_result = file.read()

with open(os.path.join(current_dir, 'fixtures/plain_nested_result')) as file:
    plain_nested_result = file.read()

with open(os.path.join(current_dir, 'fixtures/json_nested_result')) as file:
    json_nested_result = file.read()


def test_generate_diff_json():
    assert generate_diff('tests/fixtures/file1_plain.json', 'tests/fixtures/file2_plain.json') == stylish_plain_result


def test_generate_diff_yaml():
    assert generate_diff('tests/fixtures/file1_plain.yaml', 'tests/fixtures/file2_plain.yaml') == stylish_plain_result
    assert generate_diff('tests/fixtures/file1_plain.yml', 'tests/fixtures/file2_plain.yml') == stylish_plain_result


def test_generate_diff_json_stylish():
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == stylish_nested_result


def test_generate_diff_yaml_stylish():
    assert generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml') == stylish_nested_result
    assert generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml') == stylish_nested_result


def test_generate_diff_json_plain():
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'plain') == plain_nested_result


def test_generate_diff_yaml_plain():
    assert generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml', 'plain') == plain_nested_result
    assert generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml', 'plain') == plain_nested_result


def test_generate_diff_json_json():
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'json') == json_nested_result


def test_generate_diff_yaml_json():
    assert generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml', 'json') == json_nested_result
    assert generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml', 'json') == json_nested_result
