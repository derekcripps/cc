from django.contrib.auth.models import Group
from rest_framework import permissions


def is_in_group(user, group_name):
    """
    Takes a user and a group name, and returns `True` if the user is in that group.
    """
    try:
        return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()
    except Group.DoesNotExist:
        return None


class HasModelPermission(permissions.BasePermission):
    """
    Ensure user is in required groups.
    """

    def has_permission(self, request, view):
        allow_access = False
        # Get a mapping of methods -> required group.
        required_model_mapping = getattr(view, "required_model", {})

        # Determine the required groups for this particular request method.
        required_model = required_model_mapping.get(request.method, [])
        if request.user.is_superuser:
            allow_access = True
        else:
            if request.method == 'GET':
                permission_name = 'main.view_' + required_model[0].lower()
                allow_access = request.user.has_perm(permission_name)
            elif request.method == 'POST':
                permission_name = 'main.change_' + required_model[0].lower()
                allow_access = request.user.has_perm(permission_name)
            elif request.method == 'PUT':
                permission_name = 'main.add_' + required_model[0].lower()
                allow_access = request.user.has_perm(permission_name)
            elif request.method == 'DELETE':
                permission_name = 'main.delete_' + required_model[0].lower()
                allow_access = request.user.has_perm(permission_name)

        return allow_access

        # Return True if the user has all the required groups or is staff.
        #return all([is_in_group(request.user, group_name) if group_name != "__all__"
        #            else True for group_name in required_models]) or (request.user and request.user.is_staff)
