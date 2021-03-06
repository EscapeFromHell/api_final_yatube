from django.urls import include, path

from rest_framework import routers

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router_v1 = routers.DefaultRouter()
router_v1.register(prefix=r'v1/posts', viewset=PostViewSet, basename='posts')
router_v1.register(prefix=r'v1/groups',
                   viewset=GroupViewSet, basename='groups')
router_v1.register(r'v1/posts/(?P<post_id>\d+)/comments',
                   viewset=CommentViewSet, basename='comments')
router_v1.register(prefix=r'v1/follow',
                   viewset=FollowViewSet, basename='follows')

urlpatterns = [
    path('', include(router_v1.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
