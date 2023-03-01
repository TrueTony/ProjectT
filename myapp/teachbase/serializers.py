from rest_framework import serializers

from .models import Course, CourseDetails


class CourseSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseSerializerDetails(serializers.ModelSerializer):
    class Meta:
        model = CourseDetails
        fields = '__all__'
