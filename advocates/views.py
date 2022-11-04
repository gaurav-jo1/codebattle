from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Advocates
from .serializers import AdvocatesSerializer
from rest_framework.views import APIView
from rest_framework import status

# from rest_framework import mixins
# from rest_framework import generics


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


# Mixins
# class AdvocatesList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Advocates.objects.all()
#     serializer_class = AdvocatesSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class AdvocateDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Advocates.objects.all()
#     serializer_class = AdvocatesSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)