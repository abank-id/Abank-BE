from .ClientError import ClientError

class AuthenticationError(ClientError):
    def __init__(self, description):
        self.name = "AUTHENTICATION_ERROR"
        super().__init__(401, description)