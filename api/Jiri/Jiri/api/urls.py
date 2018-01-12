from django.urls import path
from django.conf.urls import include
# from rest_framework import routers

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from .views import EventViewSet, UserViewSet, api_root


event_list = EventViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
event_detail = EventViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})


urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('events/', event_list, name='event-list'),
    path('events/<int:pk>', event_detail, name='event-detail'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>', user_detail, name='user-detail'),
])


urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]

### old tuto ###
# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]