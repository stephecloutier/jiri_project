from .models import User, Event, Student
from .serializers import UserSerializer, EventSerializer, StudentSerializer
from .permissions import IsOwnerOrReadOnly, IsAdmin, IsAdminOrReadOnly

from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets

## DJR Tutorial
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
    'users': reverse('user-list', request=request, format=format),
    'events': reverse('event-list', request=request, format=format)
})


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve', 'update' and 'destroy' actions.
    """
    permission_classes = (permissions.IsAuthenticated, IsAdmin)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class StudentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve', 'update' and 'destroy' actions.
    """
    permission_classes = (permissions.IsAuthenticated, IsAdminOrReadOnly)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class EventViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve', 'update' and 'destroy' actions.
    """
    permission_classes = (permissions.IsAuthenticated, IsAdmin)
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


## old readonly for users
# class UserViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     This viewset automatically provides 'list' and 'detail' actions.
#     """
#     permission_classes = (permissions.IsAuthenticated)
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
