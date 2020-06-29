from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from api.models import ZoneCamera, CountLogData
from api.serializer import ZoneCameraSerializer


class PeopleCountUpdate(GenericAPIView):
    serializer_class = ZoneCameraSerializer

    def post(self, request, *args, **kwargs):
        cam_nam = request.data['cam_name']
        cam_object = ZoneCamera.objects.get(cam_name=cam_nam)
        _log_data = {
            'camera': cam_object,
            'count': request.data['count']
        }
        serializer = ZoneCameraSerializer(cam_object, data={'count': request.data['count'],
                                                            'last_updated': datetime.now()}, partial=True)
        if serializer.is_valid():
            serializer.save()
        else:
            return JsonResponse(data={'msg': 'Wrong Parameters'}, status=status.HTTP_400_BAD_REQUEST)

        new_log = CountLogData.objects.create(**_log_data)
        new_log.save()
        return JsonResponse(data={'date': new_log.date, 'count': new_log.count},
                        status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        try:
            cam_nam = request.GET['cam_name']
            cam_object = ZoneCamera.objects.get(cam_name=cam_nam)
            serializer = self.serializer_class(cam_object)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        except:
            return JsonResponse({'Error': 'Wrong input'}, status=status.HTTP_400_BAD_REQUEST)

