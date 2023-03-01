from django.urls import path

from .views import *

urlpatterns = [
    path('courses/get_courses/', ShowCoursesAPI.as_view()),
    path('courses/get_courses/<int:pk>', ShowCourseByIdAPI.as_view()),
    path('courses/', ShowCoursesFromDB.as_view()),
    path('courses/<int:pk>/', ShowCourseByIdFromDB.as_view()),
    path('users/create/', CreateUserAPI.as_view()),
    path('course_sessions/<int:session_id>/register/', RegisterOnSession.as_view()),
    path('courses/<int:course_id>/course_sessions/', GetCourseSessions.as_view()),
]
