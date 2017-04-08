# -*- coding: utf-8 -*-

from django.http import JsonResponse

from taiga.base import status
from taiga.auth.backends import Token # for the user fix


class RequireAuthEverywhereMiddleware(object):
    """
    This middleware intercepts all requests and responds with 401 Acess Denied in case there is no authentication data provided with the request.
    That will (a) prevent internet users from accessing the API, and (b) force the taiga frontend to show a login page, eleminating those public pages.
    Of course, the auth API itself is not affected by the change, since the users somehow need to log in.
    The admin page is also not affected, since it comes with its own authentication system.
    """

    def process_request(self, request):
        # We need to parse the auth token manually because the request.user field has not been filled yet (for some strange reason ...)
        authenticated = Token().authenticate(request) != None

        if (not authenticated) and (not request.path.startswith("/api/v1/auth")) and (not request.path.startswith("/admin")):
            return JsonResponse({"_error_type": "taiga.base.exceptions.NotAuthenticated", "_error_message": "Authentication credentials were not provided."},
                                status=status.HTTP_401_UNAUTHORIZED)
        else:
            return None
