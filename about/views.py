from os import stat
from rest_framework import generics, permissions, authentication
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .models import Bio, ContactField
from .serializers import BioSerializer, ContactFieldSerializer
from about import serializers

# Contact Fields View
class ContactFieldListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [authentication.TokenAuthentication]
    queryset = ContactField.objects.all()
    serializer_class = ContactFieldSerializer
    
    
class ContactFieldDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [authentication.TokenAuthentication]
    queryset = ContactField.objects.all()
    serializer_class = ContactFieldSerializer
    


# Bio Views
class BioAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get(self, request, *args, **kwargs):
        instance = Bio.objects.all().first()
        data = BioSerializer(instance).data
        return Response(data)
    
    def post(self, request, *args, **kwargs):
        serializer = BioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('Invalid request', status=400)
    
    def put(self, request, *args, **kwargs):
        instance = Bio.objects.all().first()
        serializer = BioSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)