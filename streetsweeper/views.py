# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from streetsweeper.models import Street
from streetsweeper.serializers import StreetSerializer

@api_view(['GET', 'POST'])
def street_list(request, format=None):
    """
    List all streets, or create a new street.
    """
    if request.method == 'GET':
        streets = Street.objects.all()
        serializer = StreetSerializer(streets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StreetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
        				status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def street_detail(request, pk, format=None):
    """
    Retrieve, update or delete a street.
    """
    try:
        street = Street.objects.get(pk=pk)
    except Street.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StreetSerializer(street)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StreetSerializer(street, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        street.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
