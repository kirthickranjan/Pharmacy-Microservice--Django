from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated
        return request.user and request.user.is_authenticated and request.user.is_admin

class IsAdminForListOrOwnerForDetail(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        
        if view.action == 'list':
            return request.user.is_admin
        return True
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_admin:
            return True
        return obj.user_email == request.user.email