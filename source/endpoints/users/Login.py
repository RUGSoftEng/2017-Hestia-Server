from flask_restplus import Resource, fields

from endpoints.error_handling import handle_standard_exception, handle_hestia_exception
from endpoints.users import namespace
from exceptions.HestiaException import HestiaException
from logic import login_logic

format_login = namespace.model("credentials", {"username": fields.String(required=True, description = "Username")
                               , "password": fields.String(required=True, description = "Password")})


@namespace.route("/login")
class Login(Resource):

    @namespace.doc("Post credentials")
    @namespace.expect(format_login)
    def post(self):
        try:
            username = namespace.apis[0].payload["username"]
            password = namespace.apis[0].payload["password"]
            token = login_logic.login_user(username, password)
        except HestiaException as error:
            return handle_hestia_exception(error)
        except Exception as error:
            return handle_standard_exception(error)

        return {"auth_token": str(token, "utf-8")}

