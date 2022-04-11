from gendiff import generate_diff


with open('tests/fixtures/result') as file:
    result = file.read()

with open('tests/fixtures/stylish_result') as file:
    stylish_result = file.read()

with open('tests/fixtures/plain_result') as file:
    plain_result = file.read()

with open('tests/fixtures/json_result') as file:
    json_result = file.read()


def test_generate_diff_json():
    assert generate_diff('tests/fixtures/file1_plain.json', 'tests/fixtures/file2_plain.json') == result


def test_generate_diff_yaml():
    assert generate_diff('tests/fixtures/file1_plain.yaml', 'tests/fixtures/file2_plain.yaml') == result
    assert generate_diff('tests/fixtures/file1_plain.yml', 'tests/fixtures/file2_plain.yml') == result


def test_generate_diff_json_stylish():
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == stylish_result


def test_generate_diff_yaml_stylish():
    assert generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml') == stylish_result
    assert generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml') == stylish_result


def test_generate_diff_json_plain():
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'plain') == plain_result


def test_generate_diff_yaml_plain():
    assert generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml', 'plain') == plain_result
    assert generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml', 'plain') == plain_result


def test_generate_diff_json_json():
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'json') == json_result


def test_generate_diff_yaml_json():
    assert generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml', 'json') == json_result
    assert generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml', 'json') == json_result
