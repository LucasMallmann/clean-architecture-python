class DuplicateUserError(Exception):
    def __init__(self) -> None:
        message = 'Duplicate user.'
        super().__init__(message)
