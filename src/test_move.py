from cmd2 import CommandResult

import cmd2_ext_test
import pytest

from cli import RobotCLI

class RobotCLI(cmd2_ext_test.ExternalTestMixin, RobotCLI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

@pytest.fixture
def robot_cli():
    """Provides an instance of the RobotCLI for tests."""
    app = RobotCLI()
    yield app
    # Any cleanup can go here if needed


def test_point_left(robot_cli):
    """Tests the 'move left' command."""
    out: CommandResult = robot_cli.app_cmd("left")
    print(out.stdout)
    assert out.stderr == ""
