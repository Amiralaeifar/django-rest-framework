from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsOwnerOrReadOnly(BasePermission):
    
    message = 'permission denied. You are not the owner'
    
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user  #request.user shouldn't be None
    
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user == obj.user 