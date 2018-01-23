from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from pprint import pprint

from .models import User, Event, Student, Project, Implementation, Meeting, Score, Performance


class UserSerializer(serializers.ModelSerializer):
    meetings = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    deleted_at = serializers.CharField(read_only=True)

    def create(self, validated_data):
        validation_errors = []
        if self.context['request'].user.is_admin:
            password = make_password(validated_data.get('password', None))
            validated_data.pop("password")
            return User.objects.create(password=password, **validated_data)
        else:
            validation_errors.append('Vous devez être administrateur pour créer un utilisateur.')
            raise serializers.ValidationError(validation_errors)

    def update(self, instance, validated_data):
        validation_errors = []
        if validated_data.get('password', None) is not None:
            instance.password = make_password(validated_data.get('password', None))
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username = validated_data.get('username', instance.username)
        instance.profile_pic = validated_data.get('profile_pic', instance.profile_pic)
        if validated_data.get('is_admin', None) is not None:
            if self.context['request'].user.is_admin:
                instance.is_admin = validated_data.get('is_admin', instance.is_admin)
            else:
                validation_errors.append('Vous devez être administrateur pour modifier votre statut admin.')

        if validation_errors:
            raise serializers.ValidationError(validation_errors)

        instance.save()
        return instance
        
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'profile_pic', 'is_admin', 'meetings', 'deleted_at')


class StudentSerializer(serializers.ModelSerializer):
    deleted_at = serializers.CharField(read_only=True)
    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'profile_pic', 'deleted_at')


class ProjectSerializer(serializers.ModelSerializer):
    deleted_at = serializers.CharField(read_only=True)
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'default_weight', 'deleted_at')

class EventSerializer(serializers.ModelSerializer):
    projects = serializers.PrimaryKeyRelatedField(many=True, queryset=Project.objects.all())
    students = serializers.PrimaryKeyRelatedField(many=True, queryset=Student.objects.all())
    users = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())
    deleted_at = serializers.CharField(read_only=True)
    class Meta:
        model = Event
        fields = ('id', 'course_name', 'exam_session', 'exam_date', 'projects', 'students', 'users', 'deleted_at')

class ImplementationSerializer(serializers.ModelSerializer):
    deleted_at = serializers.CharField(read_only=True)
    class Meta:
        model = Implementation
        fields = ('id', 'event', 'student', 'project', 'weight', 'url_project', 'url_repo', 'deleted_at')

class MeetingSerializer(serializers.ModelSerializer):
    deleted_at = serializers.CharField(read_only=True)
    user = serializers.ReadOnlyField(source='user.id')
    class Meta:
        model = Meeting
        fields = ('id', 'user', 'student', 'event', 'deleted_at')

class ScoreSerializer(serializers.ModelSerializer):
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
        instance.save()
        return instance
    class Meta:
        model = Score
        fields = ('id', 'score', 'comment', 'meeting', 'implementation', 'deleted_at')


class PerformanceSerializer(serializers.ModelSerializer):
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
        instance.save()
        return instance
            
    class Meta:
        model = Performance
        fields = ('id', 'final_score', 'student', 'event', 'deleted_at')