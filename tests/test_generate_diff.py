from gendiff import generate_diff


with open('tests/fixtures/result_plain') as file:
        answer = file.read()


def test_generate_diff_json():
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == answer


def test_generate_diff_yaml():
    assert generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml') == answer
    assert generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml') == answer
