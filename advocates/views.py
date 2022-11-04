from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Advocates
from .serializers import AdvocatesSerializer

from rest_framework.views import APIView
from rest_framework import status


# Create your views here.

# FUNCTION BASED

# @api_view(['GET'])
# def GetAdvocates(request):
#     details = Advocates.objects.all()
#     serializer = AdvocatesSerializer(details, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def GetAdvocateDetail(request,userid):
#     details = Advocates.objects.get(username=userid)
#     serializer = AdvocatesSerializer(details, many=False)
#     return Response(serializer.data)

# CLASS BASED

class AdvocatesList(APIView):

    def get(self, request, format=None):
        details = Advocates.objects.all()
        serializer = AdvocatesSerializer(details, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AdvocatesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdvocateDetail(APIView):

    def get(self, request, userid, format=None,):
        details = Advocates.objects.get(username=userid)
        serializer = AdvocatesSerializer(details, many=False)
        return Response(serializer.data)

    def put(self, request, userid, format=None):
        snippet = Advocates.objects.get(username=userid)
        serializer = AdvocatesSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, userid, format=None):
        snippet = Advocates.objects.get(username=userid)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
