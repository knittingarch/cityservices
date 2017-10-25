# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from streetsweeper.models import Neighborhood, Street
from streetsweeper.serializers import StreetSerializer


@csrf_exempt
def street_list(request):
    """
    List all streets, or create a new street.
    """
    if request.method == 'GET':
        streets = Street.objects.all()
        serializer = StreetSerializer(streets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StreetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def street_detail(request, pk):
    """
    Retrieve, update or delete a street.
    """
    try:
        street = Street.objects.get(pk=pk)
    except Street.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StreetSerializer(street)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StreetSerializer(street, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        street.delete()
        return HttpResponse(status=204)
