"""Shared API views code"""

from typing import Any

from rest_framework.response import Response
from rest_framework.views import exception_handler

from ..exceptions import RelayAPIException


class SaveToRequestUser:
    """ModelViewSet mixin for creating object for the authenticated user."""

    def perform_create(self, serializer):
        if not hasattr(self, "request"):
            raise AttributeError("self must have request attribute.")
        if not hasattr(self.request, "user"):
            raise AttributeError("self.request must have user attribute.")
        serializer.save(user=self.request.user)


def relay_exception_handler(exc: Exception, context: dict[str, Any]) -> Response | None:
    """
    Add error information to response data.

    When the error is a RelayAPIException, fields may be changed or added:

    detail - Translated to the best match from the request's Accept-Language header.
    error_code - A string identifying the error, for client-side translation.
    error_context - Additional data needed for client-side translation, if non-empty
    """
    response = exception_handler(exc, context)
    if response and isinstance(exc, RelayAPIException):
        response.data.update(exc.error_data())
    return response
