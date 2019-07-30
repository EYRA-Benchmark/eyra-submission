import pytest
import os

from click.testing import CliRunner

from eyra_tools.generate import generate


def test_generate_submission_invalid_container_id():
    runner = CliRunner()
    result = runner.invoke(generate, ['submission', 'in valid'])

    assert result.exit_code == 1


@pytest.mark.parametrize('container_type', ['submission', 'evaluation'])
def test_project_creation(container_type):
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(generate, [container_type, 'example'])

        print(result)

        assert result.exit_code == 0

        project_dir_name = os.listdir()[0]

        assert os.path.isdir(project_dir_name)
