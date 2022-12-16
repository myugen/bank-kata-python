from abc import ABCMeta


class DependencyInterface(metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'value') and
                callable(subclass.value) and
                NotImplemented)

    def value(self) -> int:
        pass


class Dependency(DependencyInterface):
    def value(self) -> int:
        return 1
