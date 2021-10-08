from rest_framework.response import Response
from rest_framework.serializers import Serializer
from system.models import TeamModel
from system.serializers import TeamSerializer
from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
class CauchView(APIView):
   
    def get(self, request):
        teamList = TeamModel.objects.all()
        Serializer = TeamSerializer(teamList, many=True)
        return Response(Serializer.data)

    

