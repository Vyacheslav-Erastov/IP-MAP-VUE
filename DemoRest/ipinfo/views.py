from django.shortcuts import render
import requests
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import IPInfo
from .serializers import IPInfoSerializer


class IPInfoView(APIView):
    def post(self, request):
        ip_list = request.data
        serializers = []
        responses = requests.post(url=f'http://ip-api.com/batch', json=ip_list).json()

        for response in responses:
            if response.get('status') == 'success':
                ip_info = IPInfo(status=response.get('status'), ip=response.get('query'), int_prov=response.get('isp'),
                                 org=response.get('org'), country=response.get('country'),
                                 region_name=response.get('regionName'),
                                 city=response.get('city'), zip=response.get('zip'), lat=response.get('lat'),
                                 lon=response.get('lon'))
                serializer = IPInfoSerializer(ip_info)
                serializers.append(serializer.data)
                ip_info.save()
            else:
                serializer = {
                    "status": response.get('status'),
                    "message": response.get('message'),
                    "query": response.get('query')
                }
                serializers.append(serializer)

        return Response(serializers)
