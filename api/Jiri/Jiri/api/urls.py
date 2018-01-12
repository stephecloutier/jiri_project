from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers

from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'events', views.EventViewSet)
router.register(r'users', views.UserViewSet)


urlpatterns = [
    path('', include(router.urls))
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]