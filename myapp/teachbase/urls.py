from django.urls import path

from .views import *

urlpatterns = [
    path('courses/get_courses/', ShowCoursesAPI.as_view(), name='get_courses'),
    path('courses/get_courses/<int:pk>', ShowCourseByIdAPI.as_view(), name='get_course_by_id'),
    path('courses/', ShowCoursesFromDB.as_view(), name='courses'),
    path('courses/<int:pk>/', ShowCourseByIdFromDB.as_view(), name='course_by_id'),
    path('users/create/', CreateUserAPI.as_view(), name='create_user'),
    path('course_sessions/<int:session_id>/register/', RegisterOnSession.as_view(), name='register_on_session'),
    path('courses/<int:course_id>/course_sessions/', GetCourseSessions.as_view(), name='course_sessions'),
]
