from .models import User, Event
from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Event
        fields = ('id', 'course_name', 'exam_session', 'exam_date', 'user')


class UserSerializer(serializers.ModelSerializer):
    events = serializers.PrimaryKeyRelatedField(many=True, queryset=Event.objects.all())
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'profile_pic', 'is_admin', 'events')

### other tuto ###
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'email', 'first_name', 'last_name', 'profile_pic', 'is_admin')