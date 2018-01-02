from rest_framework import generics
from streetsweeper.models import Street
from streetsweeper.serializers import StreetSerializer


class StreetList(generics.ListCreateAPIView):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer


class StreetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer    
