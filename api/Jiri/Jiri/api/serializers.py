from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from pprint import pprint

from .models import User, Event, Student, Project, Implementation, Meeting, Score, Performance


class UserSerializer(serializers.HyperlinkedModelSerializer):
    meetings = serializers.HyperlinkedRelatedField(many=True, view_name='meeting-detail', read_only=True)
    deleted_at = serializers.CharField(read_only=True)
    def create(self, validated_data):
        password = make_password(validated_data.get('password', None))
        validated_data.pop("password")
        return User.objects.create(password=password, **validated_data)
    def update(self, instance, validated_data):
        if validated_data.get('password', None) is not None:
            instance.password = make_password(validated_data.get('password', None))
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username = validated_data.get('username', instance.username)
        instance.profile_pic = validated_data.get('profile_pic', instance.profile_pic)
        if self.context['request'].user.is_admin:
            instance.is_admin = validated_data.get('is_admin', instance.is_admin)
        else:
            raise serializers.ValidationError('Vous devez être administrateur pour modifier votre statue admin.')
        return instance
        
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
            return Score.objects.create(score=score, **validated_data)
        else:
            raise serializers.ValidationError('Le score doit être compris entre 0 et 20 inclus.')
    def update(self, instance, validated_data):
        instance.score = validated_data.get('score', instance.score)
        if instance.score > 20 or instance.score < 0:
            raise serializers.ValidationError('Le score doit être compris entre 0 et 20 inclus.')      
        instance.comment = validated_data.get('comment', instance.comment)
        return instance
    class Meta:
        model = Score
        fields = ('id', 'score', 'comment', 'meeting', 'implementation', 'deleted_at')


class PerformanceSerializer(serializers.HyperlinkedModelSerializer):
    deleted_at = serializers.CharField(read_only=True)
    def create(self, validated_data):
        final_score = validated_data.get('final_score', None)
        if final_score <= 20 and final_score >= 0:
            validated_data.pop('final_score')
            return Performance.objects.create(final_score=final_score, **validated_data)
        else:
            raise serializers.ValidationError("Le score final doit être compris entre 0 et 20 inclus.")
    def update(self, instance, validated_data):
        instance.final_score = validated_data.get('final_score', instance.final_score)
        if instance.final_score > 20 and instance.final_score < 0:
            raise serializers.ValidationError('Le score doit être compris entre 0 et 20 inclus.')
        
        return instance
            
    class Meta:
        model = Performance
        fields = ('id', 'final_score', 'student', 'event', 'deleted_at')