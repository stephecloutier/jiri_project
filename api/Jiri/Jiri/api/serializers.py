from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from .models import User, Event, Student, Project, Implementation, Meeting, Score


class UserSerializer(serializers.HyperlinkedModelSerializer):
    meetings = serializers.HyperlinkedRelatedField(many=True, view_name='meeting-detail', read_only=True)
    deleted_at = serializers.CharField(read_only=True)
    def create(self, validated_data):
        password = make_password(validated_data.get('password', None))
        validated_data.pop("password")
        return User.objects.create(password=password, **validated_data)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'profile_pic', 'is_admin', 'meetings', 'deleted_at')


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    deleted_at = serializers.CharField(read_only=True)
    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'profile_pic', 'deleted_at')


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    deleted_at = serializers.CharField(read_only=True)
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'default_weight', 'deleted_at')

class EventSerializer(serializers.HyperlinkedModelSerializer):
    deleted_at = serializers.CharField(read_only=True)
    user = serializers.ReadOnlyField(source='user.id')
    class Meta:
        model = Event
        fields = ('id', 'course_name', 'exam_session', 'exam_date', 'user', 'deleted_at')

class ImplementationSerializer(serializers.HyperlinkedModelSerializer):
    deleted_at = serializers.CharField(read_only=True)
    class Meta:
        model = Implementation
        fields = ('id', 'event', 'student', 'project', 'weight', 'url_project', 'url_repo', 'deleted_at')

class MeetingSerializer(serializers.HyperlinkedModelSerializer):
    deleted_at = serializers.CharField(read_only=True)
    user = serializers.ReadOnlyField(source='user.id')
    class Meta:
        model = Meeting
        fields = ('id', 'user', 'student', 'event', 'deleted_at')

class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    deleted_at = serializers.CharField(read_only=True)
    def create(self, validated_data):
        score = validated_data.get('score', None)
        if score <= 20 and score >=0:
            validated_data.pop('score')
            return User.objects.create(score=score, **validated_data)
        else:
            raise serializers.ValidationError("Le score doit être compris entre 0 et 20 inclus.")
    def update(self, instance, validated_data):
        score = validated_data.get('score', None)
        if score <= 20 and score >=0:
            validated_data.pop('score')
            return User.objects.update(score=score, **validated_data)
        else:
            raise serializers.ValidationError("Le score doit être compris entre 0 et 20 inclus.")
    class Meta:
        model = Score
        fields = ('id', 'score', 'comment', 'meeting', 'implementation', 'deleted_at')