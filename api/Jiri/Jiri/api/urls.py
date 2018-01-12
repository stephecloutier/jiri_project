from django.urls import path, include
from rest_framework import routers
from Jiri.api import views

from rest_framework.urlpatterns import format_suffix_patterns
from Jiri.api import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:id>', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

### old tuto ###
# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]