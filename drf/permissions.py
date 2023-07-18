from rest_framework.permissions import SAFE_METHODS, BasePermission
from rest_framework.metadata import BaseMetadata

class IsOwnerOrReadOnly(BasePermission):
    
    message = 'permission denied. You are not the owner'
    
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user  #request.user shouldn't be None
    
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user == obj.user 
    
    

class CustomMetadata(BaseMetadata):
    
    def determine_metadata(self, request, view):
        return {
            'Name': view.get_view_name(),
            'Renderers': [renderer.media_type for renderer in view.renderer_classes],
            'Parser': [parser.media_type for parser in view.parser_classes],
        }