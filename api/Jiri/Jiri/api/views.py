from pprint import pprint
import datetime

from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework import status

from .models import User, Event, Student, Project
from .serializers import UserSerializer, EventSerializer, StudentSerializer, ProjectSerializer
from .permissions import IsOwnerOrReadOnly, IsAdmin, IsAdminOrReadOnly

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
    def destroy(self, request, pk):
        user = User.objects.get(id=pk)
        user.deleted_at = datetime.datetime.now()
        user.save()
        return Response(request.data, status=status.HTTP_204_NO_CONTENT)

class StudentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve', 'update' and 'destroy' actions.
    """
    permission_classes = (permissions.IsAuthenticated, IsAdminOrReadOnly)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def destroy(self, request, pk):
        student = Student.objects.get(id=pk)
        student.deleted_at = datetime.datetime.now()
        student.save()
        return Response(request.data, status=status.HTTP_204_NO_CONTENT)

class ProjectViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve', 'update' and 'destroy' actions.
    """
    pass

class EventViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve', 'update' and 'destroy' actions.
    """
    permission_classes = (permissions.IsAuthenticated, IsAdmin)
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def destroy(self, request, pk):
        event = Event.objects.get(id=pk)
        event.deleted_at = datetime.datetime.now()
        event.save()
        return Response(request.data, status=status.HTTP_204_NO_CONTENT)


## old readonly for users
# class UserViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     This viewset automatically provides 'list' and 'detail' actions.
#     """
#     permission_classes = (permissions.IsAuthenticated)
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
