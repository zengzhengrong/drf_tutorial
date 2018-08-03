from django.urls import re_path,include
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from rest_framework.routers import DefaultRouter

app_name = 'snippets'
'''
"""
Viewsets为url配置aciton
"""
# snippet
snippet_list = views.SnippetViewSet.as_view({'get':'list','post':'create'})
snippet_detail = views.SnippetViewSet.as_view({
	'get':'retrieve',
	'put':'update',
	'patch':'partial_update',
	'delete':'destroy'
	})
snippet_highlight = views.SnippetViewSet.as_view({
	'get':'highlight'
	},renderer_classes=[renderers.StaticHTMLRenderer])
# DjangoUser
user_list = views.UserViewSet.as_view({'get':'list'})
uer_detail = views.UserViewSet.as_view({'get':'retrieve'})

urlpatterns = format_suffix_patterns([
	re_path(r'^$', views.ApiRoot,name='api-index'),
    re_path(r'^snippets/$', snippet_list,name='snippet-list'),
    re_path(r'^snippets/(?P<pk>[0-9]+)/$', snippet_detail,name='snippet-detail'),
    re_path(r'^snippets/(?P<pk>[0-9]+)/highlight/$', snippet_highlight, name='snippet-highlight'),
    re_path(r'^users/$', user_list,name='user-list'),
    re_path(r'^users/(?P<pk>[0-9]+)/$', uer_detail,name='user-detail'),
])
'''

"""
使用rest路由器，简化ViewSets的url配置，不需要写http方法和action映射（不过在变量名称有所限制）
# 实例化rest默认路由器
# 将viewset类注册进默认路由器
# register参数（前缀，vieset，base_name=None（url命名的基本前缀'{base_name}-{url_name}'））
"""

router = DefaultRouter()
router.register(r'snippets',views.SnippetViewSet)
router.register(r'users',views.UserViewSet)

urlpatterns = [
    re_path(r'^', include(router.urls))
    ]