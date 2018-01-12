# from rest_framework import viewsets

from .models import User
from .serializers import UserSerializer
from rest_framework import generics

## DJR Tutorial

class UserList(generics.ListCreateAPIView):
    """
    List all users, or create a new user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


########## old ###########

# Create your views here.
# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

