from .models import User, Event
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse



class EventSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Event
        fields = ('id', 'course_name', 'exam_session', 'exam_date', 'user')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    events = serializers.HyperlinkedRelatedField(many=True, view_name='event-detail', read_only=True)

    def create(self, validated_data):
        password = make_password(validated_data.get('password', None))
        validated_data.pop("password")
        return User.objects.create(password=password, **validated_data)


    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'profile_pic', 'is_admin', 'events')
