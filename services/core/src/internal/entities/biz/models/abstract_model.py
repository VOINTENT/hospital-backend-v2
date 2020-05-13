from typing import Any


class AbstractModel:
    """
    Абстрактная модель, содержащая в себе общие компоненты для каждой модели
    Класс должен наследоваться всеми другими моделями
    """

    def __init__(self, id: int, created_at: Any) -> None:
        self._id = id
        self._created_at = created_at

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        self._id = value

    @property
    def created_at(self) -> Any:
        return self._created_at

    @created_at.setter
    def created_at(self, value: Any) -> None:
        self._created_at = value

