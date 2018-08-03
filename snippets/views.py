from rest_framework import generics,permissions

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer,UserSerializer
from django.contrib.auth.models import User
from .permissions import IsSnippetOwnerOrReadOnly
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import action

@api_view(['GET'])
def ApiRoot(request,format=None):
	return Response({
		'users':reverse('snippets:user-list',request=request,format=format),
		'snippets':reverse('snippets:snippet-list',request=request,format=format)
		})
'''
class SnippetList(generics.ListCreateAPIView):
	"""
	List,Create
	"""
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
	"""
	Retrieve,Update,Destroy
	"""
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsSnippetOwnerOrReadOnly)

class UserList(generics.ListAPIView):
	"""
	List
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
	"""
	Retrieve
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer

class SnippetHighlight(generics.GenericAPIView):
    """docstring for SnippetHighlight"""
    queryset = Snippet.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)
    
    def get(self,request,*args,**kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
'''


'''
Rest_framework Viewsets 自动化配置URL,viewsets继承了APIVIEW或通用视图与mixins的CRUDL方法
视图集成所有aciton，所有在app.urls里配置每个url可执行的aciton
'''

class UserViewSet(viewsets.ReadOnlyModelViewSet):
	"""自动配置django内置user{LIST,RETRIEVE}两个acitons"""
	queryset = User.objects.all()
	serializer_class = UserSerializer

class SnippetViewSet(viewsets.ModelViewSet):
	"""自动配置snippets{LIST，CREATE，RETRIEVE，UPDATE，DESTROY}五个actions"""
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsSnippetOwnerOrReadOnly)
	"""
	额外增加“highlight” action
	# 必须为非一般方法（list,create,retrieve,update,partial_update,destroy）添加@action装饰器，才能被识别并解析urlname
	"""
	@action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
	def highlight(self, request, *args, **kwargs):
		snippet = self.get_object()
		return Response(snippet.highlighted)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)