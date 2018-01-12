from django.urls import path
from django.conf.urls import include
# from rest_framework import routers

from rest_framework.urlpatterns import format_suffix_patterns
from Jiri.api import views

urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('events/', views.EventList.as_view(), name='event-list'),
    path('events/<int:pk>', views.EventDetail.as_view(), name='event-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user-detail'),
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