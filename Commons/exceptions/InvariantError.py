from .ClientError import ClientError

class InvariantError(ClientError):
    def __init__(self, description):
        self.name = "INVARIANT_ERROR"
        super().__init__(400, description)
