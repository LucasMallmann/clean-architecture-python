from src.entities.user import User
from src.usecases.errors.duplicate_user_error import DuplicateUserError
from src.usecases.errors.invalid_password_error import InvalidPasswordError


class SignUp:
    def __init__(self, user_repo, hash_service):
        self.user_repo = user_repo
        self.hash_service = hash_service

    def perform(self, user_name: str, user_email: str, user_password: str):
        if self.user_repo.find_by_email(user_email) != None:
            raise DuplicateUserError()
        if invalid(user_password):
            raise InvalidPasswordError()
        hashed_password = self.hash_service.hash(user_password)
        user = User(user_name, user_email, hashed_password)
        self.user_repo.add(user)


# Validations on uses cases
def invalid(user_password: str):
    length = len(user_password)
    if length < 6 or length > 15:
        return True
    function_names = ['islower', 'isupper', 'isdecimal']
    for function in function_names:
        if not contains_property(user_password, function):
            return True
    if not contains_special_character(user_password):
        return True
    return False


def contains_property(string, check_function):
    for c in string:
        if getattr(c, check_function)():
            return True
    return False


def contains_special_character(string: str):
    for c in string:
        if not c.isalnum():
            return True
    return False
