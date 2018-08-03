from rest_framework import permissions


class IsSnippetOwnerOrReadOnly(permissions.BasePermission):
    """只有snipper的onwer才有权限资格进行删改更新"""
    
    def has_object_permission(self, request, view, obj):
    	# SAFE_METHODS = ('GET','HEAD','OPTIONS') 也就是说这几个请求不需要通过这个类的额外许可
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # 当snipper的owner和当前认证的用户相同时才返回True
        return obj.owner == request.user