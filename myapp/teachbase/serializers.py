from rest_framework import serializers

from .models import Course, CourseDetails, Author, Type


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'


class CourseListSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)
    types = TypeSerializer(many=True)

    class Meta:
        model = Course
        fields = ['id', 'name', 'created_at', 'updated_at', 'thumb_url', 'cover_url', 'description', 'last_activity',
                  'total_score', 'total_tasks', 'unchangeable', 'include_weekly_report', 'content_type', 'is_netology',
                  'bg_url', 'video_url', 'demo', 'custom_author_names', 'custom_contents_link',
                  'hide_viewer_navigation', 'duration', 'authors', 'types']


class CourseDetailsSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)
    types = TypeSerializer(many=True)

    class Meta:
        model = CourseDetails
        fields = ['id', 'name', 'created_at', 'updated_at', 'owner_id', 'thumb_url', 'cover_url', 'description',
                  'last_activity', 'total_score', 'total_tasks', 'unchangeable', 'include_weekly_report',
                  'content_type', 'is_netology', 'bg_url', 'video_url', 'demo', 'custom_author_names',
                  'custom_contents_link', 'hide_viewer_navigation', 'duration', 'authors', 'types']
