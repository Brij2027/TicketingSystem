from rest_framework.permissions import BasePermission
from utils.db_utils import User

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        user = User.retrieve_user_detail({"username":request.user.get_username()})
        return True if user["role"] == "admin" else False