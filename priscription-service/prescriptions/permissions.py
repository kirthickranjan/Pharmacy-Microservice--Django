
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):

        # Allow READ for any authenticated user
        if request.method in SAFE_METHODS:
            return request.user and request.user.is_authenticated

        # Allow WRITE only for admin (staff)
        return (
            request.user
            and request.user.is_authenticated
            and request.user.is_staff
        )
