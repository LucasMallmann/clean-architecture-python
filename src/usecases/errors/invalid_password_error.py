class InvalidPasswordError(Exception):
    def __init__(self) -> None:
        message = 'Invalid password'
        super().__init__(message)
