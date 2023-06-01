from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    
    #True/False
    def has_object_permission(self, request, view, obj):
        if request.method in ["GET", "OPTIONS", "HEAD"] or request.user == obj.author:
            return True
        else:
            return False
