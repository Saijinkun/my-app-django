from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import UserSerializer
from django.contrib.auth.models import User


class UserApiView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()