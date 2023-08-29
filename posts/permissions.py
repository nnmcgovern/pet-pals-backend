from rest_framework import permissions


class CustomPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'POST':
            if request.user.is_authenticated:
                return True

        else:
            return True
