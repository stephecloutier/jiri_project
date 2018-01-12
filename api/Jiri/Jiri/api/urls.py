from django.urls import path
from django.conf.urls import include
# from rest_framework import routers
# from Jiri.api import views

from rest_framework.urlpatterns import format_suffix_patterns
from Jiri.api import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
    path('events/', views.EventList.as_view()),
    path('events/<int:pk>', views.EventDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]

### old tuto ###
# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]