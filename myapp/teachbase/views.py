import requests
from django.http import Http404
from rest_framework.generics import ListAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Course
from .serializers import CourseSerializerList, CourseSerializerDetails
from myapp.settings import CLIENT_ID, CLIENT_SECRET, TEACHBASE_URL
from client.client import TeachbaseClient

teachbase = TeachbaseClient(CLIENT_ID, CLIENT_SECRET, TEACHBASE_URL)


class ShowCoursesAPI(ListAPIView):
    queryset = teachbase.get_all_courses()
    serializer_class = CourseSerializerList


class ShowCourseByIdAPI(RetrieveAPIView):
    serializer_class = CourseSerializerDetails

    def get_object(self):
        course = teachbase.get_one_course(self.kwargs['pk'])
        if type(course) == int:
            raise Http404
        return course


class ShowCoursesFromDB(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializerList


class ShowCourseByIdFromDB(RetrieveAPIView):
    serializer_class = CourseSerializerList

    def get_object(self):
        return get_object_or_404(Course, pk=self.kwargs['pk'])


class CreateUserAPI(APIView):

    def post(self, request):
        teachbase.check_token_is_alive()
        params = {
            'access_token': teachbase.access_token
        }
        user = {
            'users': [
                {
                    'email': 'test@teachbase.ru',
                    'name': 'John',
                    'description': 'Corrupti natus quia recusandae.',
                    'last_name': 'Doe',
                    'phone': 'string',
                    'role_id': 1,
                    'auth_type': 0,
                    'external_id': 'u-00888',
                    'labels': {
                        '1': '2',
                        '3': '4'
                    },
                    'password': 'qwerty',
                    'lang': 'ru'
                }
            ],
            'external_labels': True,
            'options': {
                'activate': True,
                'verify_emails': True,
                'skip_notify_new_users': True,
                'skip_notify_active_users': True
            }
        }
        response = requests.post(f'{teachbase.base_url}/endpoint/v1/users/create',
                                 params=params, json=user)

        if response.status_code != 200:
            return Response(status=response.status_code)
        return Response(response.json())


class RegisterOnSession(APIView):

    def post(self, request, session_id):
        teachbase.check_token_is_alive()
        params = {
            'access_token': teachbase.access_token
        }
        user = {
            'email': 'test@teachbase.ru',
            'phone': 792177788666,
            'user_id': 105680
        }
        response = requests.post(f'{teachbase.base_url}/endpoint/v1/course_sessions/{session_id}/register',
                                 params=params, json=user)

        if response.status_code != 200:
            return Response(status=response.status_code)
        return Response(response)


class GetCourseSessions(APIView):

    def get(self, request, course_id):
        teachbase.check_token_is_alive()
        params = {
            'access_token': teachbase.access_token,
            'page': 1,
            'per_page': 3,
            'filter': 'active',
            'participant_ids': None
        }
        response = requests.get(f'{teachbase.base_url}/endpoint/v1/courses/{course_id}/course_sessions',
                                params=params)

        if response.status_code != 200:
            return Response(status=response.status_code)
        return Response(response.json())
