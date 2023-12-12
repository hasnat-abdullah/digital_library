from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.exceptions import APIException


class AuthenticationFailed(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _("Unable to log in with provided credentials..")
    default_code = "authentication_failed"


class InstanceNotFound(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _("Instance is not found.")
    default_code = "instance_not_found"


class ExpectedFieldNotAvailableInRequest(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _("Required field is not available in the request body.")
    default_code = "expected_field_not_available"


class WrongDataFormat(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _("Required field is not available in the request body.")
    default_code = "expected_field_not_available"


class SessionExpired(APIException):
    status_code = 440  # Session expired http status code
    default_detail = _("The session is expired. Login again or refresh token.")
    default_code = "session_expired"


class UnknownError(APIException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    default_detail = _("Something went wrong.")
    default_code = "unknown_error"


class TokenError(APIException):
    status_code = 440  # Session expired http status code
    default_detail = _("The token is invalid/expired. Login again or refresh token.")
    default_code = "token_expired"
