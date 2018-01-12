from .models import User, Event
from rest_framework import serializers


class EventSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Event
        fields = ('url', 'id', 'course_name', 'exam_session', 'exam_date', 'user')


class UserSerializer(serializers.HyperLinkedModelSerializer):
    events = serializers.HyperlinkedRelatedField(many=True, view_name='event-detail', read_only=True)
    class Meta:
        model = User
        fields = ('url', 'username', 'first_name', 'last_name', 'profile_pic', 'is_admin', 'events')

### other tuto ###
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'email', 'first_name', 'last_name', 'profile_pic', 'is_admin')