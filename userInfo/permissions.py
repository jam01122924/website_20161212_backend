from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class OnlyOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to view and edit it
    """
    def has_object_permission(self, request, view, obj):
        # all permission is only allowed to the owner
        return obj.owner == request.user


class OnlyAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff


# class OnlyAdminOrOwner(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.user.is_anonymous():
#             return False
#         return True
#
#     def has_object_permission(self, request, view, obj):
#         return request.user.is_staff or obj == request.user or (obj.owner and obj.owner == request.user)


class OnlyAdminOrOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return view.action == 'retrieve' or view.action == 'list' or request.user.is_staff

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj == request.user or (obj.owner and obj.owner == request.user)
