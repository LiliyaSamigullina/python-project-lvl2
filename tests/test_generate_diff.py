from gendiff import generate_diff


def test_generate_diff():
    with open('tests/fixtures/result_json') as file:
        answer = file.read()
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == answer