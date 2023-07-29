from werkzeug.exceptions import HTTPException

class ClientError(Exception):
    def __init__(self, code, description):
        self.code = 400
        self.description = description

    