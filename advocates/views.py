from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Advocates
from .serializers import AdvocatesSerializer

# Create your views here.
@api_view(['GET'])
def getAdvocates(request):
    details = Advocates.objects.all()
    serializer = AdvocatesSerializer(details, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getAdvocateDetail(request,userid):
    details = Advocates.objects.get(username=userid)
    serializer = AdvocatesSerializer(details, many=False)
    return Response(serializer.data)