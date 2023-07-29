from .ClientError import ClientError

class NotFoundError(ClientError):
    def __init__(self, description):
        self.name = "NOT_FOUND_ERROR"
        super().__init__(404, description)