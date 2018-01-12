from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from . import views

schema_view = get_schema_view(title='Pastebin API')

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'events', views.EventViewSet)
router.register(r'users', views.UserViewSet)


urlpatterns = [
    path('schema/', schema_view),
    path('', include(router.urls))
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]