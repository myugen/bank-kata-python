from unittest.mock import MagicMock, Mock

from src.dependency import Dependency, DependencyInterface
from src.kata import Kata


class TestKata:
    def test_value_should_work_with_dependency_implementation(self):
        dependency = Dependency()
        kata = Kata(dependency)

        actual = kata.value()

        assert actual == 1

    def test_value_should_work_with_mocked_dependency(self):
        mocked_dependency: DependencyInterface = Mock()
        mocked_dependency.value = MagicMock(return_value=42)
        kata = Kata(mocked_dependency)

        actual = kata.value()

        assert actual == 42
        mocked_dependency.value.assert_called_once()
