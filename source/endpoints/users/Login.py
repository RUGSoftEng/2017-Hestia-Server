from flask_restplus import Resource, namespace, fields

from endpoints.error_handling import handle_standard_exception, handle_hestia_exception
from exceptions import HestiaException
from logic import login_logic

format_login = namespace.model({"username": fields.String(required = True, description = "Username")
                                , "password" : fields.String(required = True, description = "Password")})


@namespace.route("/login")
class Login(Resource):

    @namespace.marshal_with(format_login)
    def post(self):
        try:
            username = namespace.apis[0].payload["username"]
            password = namespace.apis[0].payload["password"]
            token = login_logic.login_user(username, password)
        except HestiaException as error:
            return handle_hestia_exception(error)
        except Exception as error:
            return handle_standard_exception(error)

        return {"auth_token": token}

