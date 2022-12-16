from src.dependency import DependencyInterface


class Kata:
    dependency: DependencyInterface = None

    def __init__(self, dependency: DependencyInterface) -> None:
        self.dependency = dependency
        super().__init__()

    def value(self) -> int:
        return self.dependency.value()
