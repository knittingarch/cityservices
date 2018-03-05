from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from streets.models import Street
from streets.permissions import IsOwnerOrReadOnly
from streets.serializers import (
    StreetSerializer,
    UserSerializer,
)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'streets': reverse('street-list', request=request, format=format)
    })


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class StreetList(generics.ListCreateAPIView):
    """
    List all streets, or create a new street.
    """
    queryset = Street.objects.all()
    serializer_class = StreetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class StreetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a snippet instance.
    """
    queryset = Street.objects.all()
    serializer_class = StreetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,)
