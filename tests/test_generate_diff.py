from gendiff import generate_diff
from gendiff.formatters.stylish import format_stylish


with open('tests/fixtures/result_plain') as file:
    plain_answer = file.read()

with open('tests/fixtures/result') as file:
    answer = file.read()


def test_generate_diff_plain_json():
    assert generate_diff('tests/fixtures/file1_plain.json', 'tests/fixtures/file2_plain.json') == plain_answer


def test_generate_diff_plain_yaml():
    assert generate_diff('tests/fixtures/file1_plain.yaml', 'tests/fixtures/file2_plain.yaml') == plain_answer
    assert generate_diff('tests/fixtures/file1_plain.yml', 'tests/fixtures/file2_plain.yml') == plain_answer


def test_generate_diff_json():
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == answer


def test_generate_diff_yaml():
    assert generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml') == answer
    assert generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml') == answer
