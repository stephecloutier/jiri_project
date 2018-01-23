from pprint import pprint
import datetime
import json
# import io

from rest_framework import generics
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import api_view, detail_route, list_route
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework import status

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .models import User, Event, Student, Project, Implementation, Meeting, Score, Performance
from .serializers import UserSerializer, EventSerializer, StudentSerializer, ProjectSerializer, ImplementationSerializer, MeetingSerializer, ScoreSerializer, PerformanceSerializer
from .permissions import IsOwnerOrReadOnly, IsAdmin, IsAdminOrReadOnly, IsAdminOrOwnerOfScore, IsAdminOrOwner

# Auth token + user ID
class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})



## DJR Tutorial
@api_view(['GET'])
# @authentication_classes((SessionAuthentication, TokenAuthentication))
def api_root(request, format=None):
    return Response({
    'users': reverse('user-list', request=request, format=format),
    'students': reverse('student-list', request=request, format=format),
    'projects': reverse('project-list', request=request, format=format),
    'events': reverse('event-list', request=request, format=format),
    'implementations': reverse('implementation-list', request=request, format=format),
    'meetings': reverse('meeting-list', request=request, format=format),
    'scores': reverse('score-list', request=request, format=format),
    'performances': reverse('performance-list', request=request, format=format),
})


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve', 'update' and 'destroy' actions.
    """
    permission_classes = (permissions.IsAuthenticated, IsAdminOrOwner)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def destroy(self, request, pk):
        user = User.objects.get(id=pk)
        user.deleted_at = datetime.datetime.now()
        user.save()
        return Response(request.data, status=status.HTTP_204_NO_CONTENT)
    @list_route()
    def event(self, request):
        event = User.objects.filter(event__id=request.query_params.get('event', None))
        serializer = self.get_serializer(event, many=True)
        return Response(serializer.data)

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
    @list_route()
    def event(self, request):
        event = Student.objects.filter(event__id=request.query_params.get('event', None))
        serializer = self.get_serializer(event, many=True)
        return Response(serializer.data)

class ProjectViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve', 'update' and 'destroy' actions.
    """
    permission_classes = (permissions.IsAuthenticated, IsAdminOrReadOnly)
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    def destroy(self, request, pk):
        project = Project.objects.get(id=pk)
        project.deleted_at = datetime.datetime.now()
        project.save()
        return Response(request.data, status=status.HTTP_204_NO_CONTENT)
    @list_route()
    def event(self, request):
        event = Project.objects.filter(event__id=request.query_params.get('event', None))
        serializer = self.get_serializer(event, many=True)
        return Response(serializer.data)

class EventViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve', 'update' and 'destroy' actions.
    """
    permission_classes = (permissions.IsAuthenticated, IsAdminOrReadOnly)
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    pprint(Event.objects.all())
    def destroy(self, request, pk):
        event = Event.objects.get(id=pk)
        event.deleted_at = datetime.datetime.now()
        event.save()
        return Response(request.data, status=status.HTTP_204_NO_CONTENT)

class ImplementationViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve', 'update' and 'destroy' actions.
    """
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Implementation.objects.all()
    serializer_class = ImplementationSerializer

    def destroy(self, request, pk):
        implementation = Implementation.objects.get(id=pk)
        implementation.deleted_at = datetime.datetime.now()
        implementation.save()
        return Response(request.data, status=status.HTTP_204_NO_CONTENT)
    @list_route()
    def student(self, request):
        student = Implementation.objects.filter(student__id=request.query_params.get('student', None), event__id=request.GET.get('event', None))
        serializer = self.get_serializer(student, many=True)
        return Response(serializer.data)
    @list_route(methods=['post'])
    def addAll(self, request):
        implementations = request.data['implementations']
        pprint(implementations)
        if request.method == 'POST' and implementations:
            for implementation in implementations:
                serializer = ImplementationSerializer(data=implementation)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(implementations, status=status.HTTP_201_CREATED)
 

        

class MeetingViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve', 'update' and 'destroy' actions.
    """
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def destroy(self, request, pk):
        meeting = Meeting.objects.get(id=pk)
        meeting.deleted_at = datetime.datetime.now()
        meeting.save()
        return Response(request.data, status=status.HTTP_204_NO_CONTENT)
    @list_route()
    def user(self, request):
        # pprint('RAWAWRWRRWRWRWRWRAAWWWWRRRRRR')
        # pprint(request.GET.get('event', None))
        user = Meeting.objects.filter(user__id=request.user.id, event__id=request.query_params.get('event', None))
        serializer = self.get_serializer(user, many=True)
        return Response(serializer.data)

class ScoreViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve', 'update' and 'destroy' actions.
    """
    permission_classes = (permissions.IsAuthenticated, IsAdminOrOwnerOfScore)
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

    def destroy(self, request, pk):
        score = Score.objects.get(id=pk)
        score.deleted_at = datetime.datetime.now()
        score.save()
        return Response(request.data, status=status.HTTP_204_NO_CONTENT)

class PerformanceViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve', 'update' and 'destroy' actions.
    """
    permission_classes = (permissions.IsAuthenticated, IsAdmin)
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer

    def destroy(self, request, pk):
        performance = Performance.objects.get(id=pk)
        performance.deleted_at = datetime.datetime.now()
        performance.save()
        return Response(request.data, status=status.HTTP_204_NO_CONTENT)

    @list_route()
    def student(self, request):
        student = Implementation.objects.filter(student__id=request.query_params.get('student', None), event__id=request.GET.get('event', None))
        serializer = self.get_serializer(student, many=True)
        return Response(serializer.data)
