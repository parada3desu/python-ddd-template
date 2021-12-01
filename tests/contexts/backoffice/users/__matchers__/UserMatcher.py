from src.contexts.backoffice.users.domain.entities.User import User


class UserMatcher:

    def __init__(self, user: User):
        self.user = user

    def __eq__(self, user2: User):
        user1 = self.user
        return user1.id.value() == user2.id.value() and \
            user1.name.value() == user2.name.value()
