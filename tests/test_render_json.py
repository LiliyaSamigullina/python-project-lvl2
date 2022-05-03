import pytest
from gendiff import generate_diff

FORMATTER = 'json'


@pytest.mark.asyncio
async def test_json(file1_json_path, file2_json_path, result_render):
    assert result_render == generate_diff(file1_json_path, file2_json_path, FORMATTER)


@pytest.mark.asyncio
async def test_yaml(file1_yaml_path, file2_yaml_path, result_render):
    assert result_render == generate_diff(file1_yaml_path, file2_yaml_path, FORMATTER)


@pytest.mark.asyncio
async def test_yml(file1_yml_path, file2_yml_path, result_render):
    assert result_render == generate_diff(file1_yml_path, file2_yml_path, FORMATTER)
