from rest_framework import status
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
    # Now add the HTTP status code to the response.
    if response is not None:
        data = {'is_success_response': False}
        # non field error
        if "detail" in response.data:
            data["code"] = "non_field_error"
            data["details"] = {}
            if response.status_code == status.HTTP_401_UNAUTHORIZED and "messages" in response.data:
                data["details"] = response.data.pop("messages")[0]
            else:
                data["details"]["message"] = response.data.pop("detail")
        # field error
        else:
            data["code"] = "field_error"
            data["details"] = {}
            for field, message in response.data.items():
                if isinstance(message, list):
                    data["details"][field] = message
                elif isinstance(message, str):
                    data["details"][field] = [message]
                else:
                    raise AssertionError(
                        "Field type error:: error field value is not list or string!!!"
                    )
        response.data = data
    return response
