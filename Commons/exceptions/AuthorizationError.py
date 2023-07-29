from .ClientError import ClientError

class AuthorizationError(ClientError):
    def __init__(self, description):
        self.name = "AUTHORIZATION_ERROR"
        super().__init__(403, description)