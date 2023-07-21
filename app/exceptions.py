class CharacterNoLongerAvailable(Exception):
    def __init__(self, message):
        super().__init__(message)


class ResponseGenerationException(Exception):
    def __init__(self, message):
        super().__init__(message)
