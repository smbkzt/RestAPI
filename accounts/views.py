from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.serializers import UserSerializer


class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self):
        pass
