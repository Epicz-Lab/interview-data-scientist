from abc import ABC, abstractmethod

from app.models.user import User


class UserRepository(ABC):
    @abstractmethod
    def get_users(self) -> list[User]:
        ...
