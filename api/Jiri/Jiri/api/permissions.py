from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owner of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.  
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the user (owner) of the object
        return obj.user == request.user

class IsAdmin(permissions.BasePermission):
    """
    Custom permission to only allow admin users to access and edit a resource.
    """

    message = 'Vous devez être administrateur pour accéder à cette vue.'
    def has_permission(self, request, view):
        return request.user.is_admin


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admin users to edit a resource.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user.is_admin


class IsAdminOrOwnerOfScore(permissions.BasePermission):
    """
    Custom permission ton only allow admin or owner to edit an object
    """

    def has_object_permission(self, request, view, obj):
        return obj.meeting.user == request.user or request.user.is_admin