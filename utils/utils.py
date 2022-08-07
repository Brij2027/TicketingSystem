from django.contrib.auth.base_user import BaseUserManager

class UrlUtils:

    # user urls
    USER_CREATE = "user_create"

    # ticket urls
    TICKET_CREATE = "ticket_create"
    TICKET_LIST = "ticket_list"
    TICKET_GET = "ticket_get"

class Utils:

    @staticmethod
    def generate_random_password():
        return BaseUserManager().make_random_password(10)
