from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        print(obj)
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
            
        # if request.method in permissions.SAFE_METHODS:
        #     return True

        # # Instance must have an attribute named `owner`.
        # return obj.owner == request.user
    
        if request.method == 'GET':
            return True
        
        if request.user == obj.title:
            return True
        else:
            return False