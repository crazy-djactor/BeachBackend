import base64
from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response

from api.models import Zone, CountLogData, Beach
from api.serializer import ZoneCameraSerializer, BeachSerializer


class BeachDetailView(GenericAPIView):
    serializer_class = ZoneCameraSerializer

    def get_queryset(self):
        try:
            beach_id = self.kwargs.get('pk')
            zone_cams = Zone.objects.filter(beach_id=beach_id)
            return zone_cams
        except:
            return []

    def get(self, request, *args, **kwargs):
        try:
            query_set = self.get_queryset()
            serializer = self.serializer_class(query_set, many=True)
            cam_list = serializer.data.copy()
            return JsonResponse({'cam_count': len(cam_list),
                                 'list': cam_list}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({'Error': 'Wrong Input'}, status=status.HTTP_400_BAD_REQUEST)


class ZomeView(GenericAPIView):
    serializer_class = ZoneCameraSerializer

    def get_queryset(self):
        try:
            cam_name = self.kwargs.get('cam_name')
            cam = Zone.objects.get(zone_name=cam_name)
            return cam
        except:
            return None

    @staticmethod
    def img_decode_b64(img_date, img_name):
        img_out = open(img_name, 'wb')
        img_out.write(base64.b64decode(img_date))
        img_out.close()

    def post(self, request, *args, **kwargs):
        cam_object = self.get_queryset()
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
            cam_obj = self.get_queryset()
            serializer = self.serializer_class(cam_obj)
            obdata = serializer.data.copy()
            return JsonResponse(obdata, status=status.HTTP_200_OK)
        except:
            return JsonResponse({'Error': 'Wrong input'}, status=status.HTTP_400_BAD_REQUEST)


class BeachZoneListView(ListAPIView):
    queryset = Beach.objects.all()
    serializer_class = BeachSerializer
    # def get(self, request, *args, **kwargs):
    #     try:
    #         query_set = self.get_queryset()
    #         serializer = self.serializer_class(query_set, many=True)
    #         return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    #     except:
    #         return JsonResponse({'Error': 'Wrong Input'}, status=status.HTTP_400_BAD_REQUEST)


class BeachZoneView(GenericAPIView):
    serializer_class = ZoneCameraSerializer
