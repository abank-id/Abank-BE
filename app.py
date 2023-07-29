# secrets
from dotenv import dotenv_values

secret = dotenv_values(".env")

# database
from Infrastructure.database import Database

print(secret["DB_USERNAME"])

database = Database(
    user=secret["DB_USERNAME"],
    password=secret["DB_PASSWORD"],
    host=secret["DB_HOST"],
    port=secret["DB_PORT"],
    database=secret["DB_DATABASE"],
    ssl_ca=secret["DB_SSL_CA"],
    ssl_disabled=False,
)

# app
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)

# Repositories
from Infrastructure.repository import (
    UserRepository,
    FamilyRepository,
    FamilyMemberRepository,
    DailyCashRepository,
)

user = UserRepository(database)
family = FamilyRepository(database)
familyMember = FamilyMemberRepository(database)
dailyCash = DailyCashRepository(database)

# User handlers
from Interface.http.api import (
    UserHandler,
    FamilyHandler,
    FamilyMemberHandler,
    DailyCashHandler,
)

userHandler = UserHandler(user)
familyHandler = FamilyHandler(family)
familyMemberHandler = FamilyMemberHandler(familyMember)
dailyCashHandler = DailyCashHandler(dailyCash)

# Routes
# User routes
app.add_url_rule(
    "/users",
    endpoint="userHandler.postUser",
    view_func=userHandler.postUser,
    methods=["POST"],
)

# Family Routes
app.add_url_rule(
    "/family",
    endpoint="familyHandler.postFamily",
    view_func=familyHandler.postFamily,
    methods=["POST"],
)

app.add_url_rule(
    "/family",
    endpoint="familyHandler.putFamily",
    view_func=familyHandler.putFamily,
    methods=["PUT"],
)

# Family Member Routes
app.add_url_rule(
    "/family/<int:family_id>/member",
    endpoint="familyMemberHandler.postFamilyMember",
    view_func=familyMemberHandler.postFamilyMember,
    methods=["POST"],
)

# Daily Cash Routes
app.add_url_rule(
    "/users/<int:user_id>",
    endpoint="dailyCashHandler.postDailyCash",
    view_func=dailyCashHandler.postDailyCash,
    methods=["POST"],
)


# Error handler
from flask import jsonify
from Commons.exceptions import InvariantError


@app.errorhandler(400)
def bad_request(e):
    return jsonify({"status": "error", "message": f"bad request {e}"}), 400


@app.errorhandler(InvariantError)
def handle_exception(e):
    return jsonify({"status": "error", "message": str(e)}), e.code
