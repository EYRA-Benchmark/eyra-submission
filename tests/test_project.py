import pytest
import os
import plumbum

from pathlib import Path
from plumbum.cmd import bash, python


@pytest.fixture
def template_dir():
    return Path(__file__).parent.parent / "eyra_tools" / "template"


@pytest.mark.parametrize('ctype', ['submission', 'evaluation'])
def test_project_container_type(ctype, template_dir, cookies):
    project = cookies.bake(template=str(template_dir.absolute()),
                           extra_context={'container_name': 'example',
                                          'container_type': ctype})
    print(template_dir)

    assert project.exit_code == 0
    assert project.exception is None
    assert project.project.basename.startswith('example')
    assert project.project.isdir()


def test_input_data_removal_submission(template_dir, cookies):
    project = cookies.bake(template=str(template_dir.absolute()),
                           extra_context={'container_name': 'example',
                                          'container_type': 'submission'})
    print(template_dir)

    data_dir = Path(str(project.project))/'data'/'input'

    assert os.path.isfile(str(data_dir/'test_data'))
    assert not os.path.isfile(str(data_dir/'ground_truth'))
    assert not os.path.isfile(str(data_dir/'implementation_output'))


def test_input_data_removal_evaluation(template_dir, cookies):
    project = cookies.bake(template=str(template_dir.absolute()),
                           extra_context={'container_name': 'example',
                                          'container_type': 'evaluation'})
    print(template_dir)

    data_dir = Path(str(project.project))/'data'/'input'

    assert not os.path.isfile(str(data_dir/'test_data'))
    assert os.path.isfile(str(data_dir/'ground_truth'))
    assert os.path.isfile(str(data_dir/'implementation_output'))


@pytest.mark.parametrize('ctype', ['submission', 'evaluation'])
def test_run_code_locally(ctype, template_dir, cookies):
    project = cookies.bake(template=str(template_dir.absolute()),
                           extra_context={'container_name': 'example',
                                          'container_type': ctype})
    cwd = os.getcwd()
    os.chdir(str(project.project))

    # run script src/[submission|evaluation].py
    try:
        python(Path('src')/'{}.py'.format(ctype))
    except plumbum.ProcessExecutionError as e:
        pytest.fail(e)
    finally:
        os.chdir(cwd)

    # test output
    out = project.project.join('data', 'output')
    assert os.path.isfile(str(out))


@pytest.mark.parametrize('ctype', ['submission', 'evaluation'])
def test_run_test_sh(ctype, template_dir, cookies):
    container_name = 'eyratools_pytest_container'
    project = cookies.bake(template=str(template_dir.absolute()),
                           extra_context={'container_name': container_name,
                                          'container_type': ctype})
    cwd = os.getcwd()
    os.chdir(str(project.project))

    # run script
    try:
        bash('test.sh')
    except plumbum.ProcessExecutionError as e:
        pytest.fail(e)
    finally:
        os.chdir(cwd)

    # test output
    out = project.project.join('data', 'output')
    assert os.path.isfile(str(out))


